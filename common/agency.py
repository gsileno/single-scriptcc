from common.messages import Belief, DesireWithStrength, CommandWithStrength, SpeechActForce
from common.memories import EmbodiedDatabase
from functools import partial

import logging

logging.basicConfig(filename='agency.log', filemode='w', level=logging.INFO)


# various helpers for string-based processing

def is_primitive_invocation(invocation):
    return invocation[0] == "#"


def is_maintenance_goal_invocation(invocation):
    return is_goal_invocation(invocation) and invocation[1] == "!"


def is_procedural_goal_invocation(invocation):
    return is_goal_invocation(invocation) and invocation[1] == "@"


def is_achievement_goal_invocation(invocation):
    return is_goal_invocation(invocation) and \
           not is_maintenance_goal_invocation(invocation) and \
           not is_procedural_goal_invocation(invocation)


def is_goal_invocation(invocation):
    return invocation[0] == "!"


def is_perceptual(invocation):
    return not is_goal_invocation(invocation) and not is_primitive_invocation(invocation)


def is_neg_perceptual(invocation):
    return is_perceptual(invocation) and invocation[0] == "~"


class Thread:

    def __init__(self, controller_agent, rule, ranking):
        """a thread is run by a controller agent, has possibly a controller thread, was invocated and has a ranking.
        it is specified together with instructions, an instruction counter, and can be locked, in which case it generates
        the associated unlocking and timeout messages."""
        self.controller_agent = controller_agent
        self.rule = rule
        self.ranking = ranking

        self.instructions = []
        self.locked = False
        self.pos = 0

    def lock(self):
        self.print("locking thread %s" % self)
        self.locked = True

    def unlock(self):
        self.print("unlocking thread %s" % self)
        self.locked = False

    def next(self):
        if self.pos == len(self.instructions):
            return None
        else:
            f = self.instructions[self.pos]
            self.pos += 1
        return f


    def send_body_signal(self, message):
        if message.force == SpeechActForce.DIRECTIVE:
            command = message.functor[1:]
            self.print("sending signal to body: %s" % command)
            self.controller_agent.body.initiate_process(
                command,
                self.unlock
            )
            self.lock()
        else:
            raise RuntimeError("Not applicable")


    def send_mental_signal(self, message):
        self.print("sending signal to mind: %s" % message)
        if message.force == SpeechActForce.PROMISE:
            # check whether the goal has already been achieved:

            percept_query = self.controller_agent.build_query(message.functor)
            if percept_query():
                pass
                self.print("%s already achieved." % message.functor)
            else:
                # find applicable rule
                rule = self.controller_agent.find_applicable_rule(message.functor)

                if rule is not None:
                    self.lock()
                    thread = self.controller_agent.append_thread(rule, self.ranking)  # the derived thread inherit the same ranking # TODO: params
                    self.print("intentional stack: %s " % str(self.controller_agent.intentional_stack))
                    thread.run()
                else:
                    self.print("found no applicable rule")
                    self.fail()
        else:
            raise RuntimeError("To be implemented")

    def fail(self):
        raise RuntimeError("To be implemented")

    def resume(self):
        self.unlock()
        self.print("resume thread %s" % self)
        self.controller_agent.intentional_stack.pop() # remove child
        self.run()

    def complete(self):
        self.print("complete thread %s" % self)
        if len(self.controller_agent.intentional_stack) > 1:
            parent_thread = self.controller_agent.intentional_stack[-2]
            parent_thread.resume()
        else:
            self.print("remove thread %s" % self)
            self.controller_agent.intentional_stack = []

    def run(self):
        f = self.next()
        if f is None:
            self.complete()
        else:
            f()

    def __str__(self):
        return "%s:%d" % (self.rule, self.pos)

    def __repr__(self):
        return self.__str__()

    def print(self, text):
        logging.info("%s || %s > %s " % (self.controller_agent.body.name, str(self), text))


class EntityWithMessageQueue:
    """an entity with a message queue, that can receive and send messages"""

    def __init__(self):
        self.queue = []

    def send_message(self, target, message):
        if not isinstance(target, EntityWithMessageQueue):
            raise RuntimeError("\"%s\" is not a valid ReactiveEntity." % (target))
        return target.queue.append(message)

    def push(self, message):
        return self.queue.append(message)

    def pop(self):
        return self.queue.pop()

    def received(self, message):
        return self.queue.pop(message)

    def flush(self):
        self.queue = []


class IntentionalAgent(EntityWithMessageQueue):
    """An intentional agent is a reactive entity with a deliberation cycle exploiting a belief base and an intentional stack"""

    def __init__(self, body, beliefsbase_type):
        super().__init__()

        if body is None:
            raise RuntimeError("An agent needs a body.")
        if not issubclass(beliefsbase_type, EmbodiedDatabase):
            raise RuntimeError("Not valid type for the belief base.")
        elif type(beliefsbase_type) == EmbodiedDatabase:
            raise UserWarning("You are using a belief base with no perceptual rules.")

        self.body = body
        self.beliefs = beliefsbase_type(body)
        self.intentional_stack = []

    def print(self, text):
        logging.info("%s || %s " % (str(self.body.name), text))

    def build_query(self, invocation):
        query_function = partial(self.beliefs.query, Belief(invocation))
        return query_function

    def build_query_conditions(self, invocation):
        raw_trigger_conditions = self.rule_to_conditions()
        if invocation not in raw_trigger_conditions:
            return None
        else:
            raw_conditions = raw_trigger_conditions[invocation]
            if len(raw_conditions) == 1:
                query_function = self.build_query(raw_conditions[0])
            else:
                raise RuntimeError("Not yet implemented")
            return query_function

    def allocate_instructions(self, thread):
        # print("allocating instructions for %s" % (str(thread)))

        dict_trigger_actions = self.rule_to_actions()
        raw_actions = dict_trigger_actions[thread.rule]

        instructions = []
        for raw_action in raw_actions:
            if is_primitive_invocation(raw_action):
                instructions.append(
                    partial(
                        thread.send_body_signal,
                        CommandWithStrength(thread.ranking, raw_action)
                    )
                )
            else:
                instructions.append(
                    partial(
                        thread.send_mental_signal,
                        DesireWithStrength(thread.ranking, raw_action)
                    )
                )
        thread.instructions = instructions

    def append_thread(self, invocation, ranking):
        thread = Thread(self, invocation, ranking)
        self.allocate_instructions(thread)
        self.intentional_stack.append(thread)
        return thread

    def get_rules(self, goal):
        dict_goal_rules = self.goal_to_rules()
        if goal in dict_goal_rules:
            return dict_goal_rules[goal]
        else:
            return [goal]  # default behaviour

    def get_ranking(self, invocation):
        return self.rule_to_ranking()[invocation]

    def get_higherly_ranked_perceptual_invocations(self, ranking):
        relevant_invocations = []
        invocation_to_ranking = self.rule_to_ranking()
        for invocation in invocation_to_ranking.keys():
            if is_perceptual(invocation):
                if ranking is None or invocation_to_ranking[invocation] > ranking:
                    relevant_invocations.append(invocation)
        return relevant_invocations

    def find_applicable_rule(self, invocation):
        rules = self.get_rules(invocation)
        for rule in rules:
            applicability_query = self.build_query_conditions(rule)
            if applicability_query is None or applicability_query():
                # print("applicability confirmed with rule '%s'" % str(rule))
                return rule
        return None

    # procedural and preferential knowledge

    @classmethod
    def rule_to_conditions(cls):
        return {}

    @classmethod
    def rule_to_actions(cls):
        return {}

    @classmethod
    def rule_to_ranking(cls):
        return {}

    @classmethod
    def goal_to_rules(cls):
        return {}

    # execution cycle, similar to kernel/user mode in operating systems

    def kernel_mode(self):
        self.print("entering in kernel mode..")

        thread, ranking = self.current_thread_ranking()

        if ranking != 0:  # 0 is the maximal ranking (ranking decreases with increasing numbers)
            # look for possibly more relevant events (only on perceptual triggers)
            relevant_invocations = self.get_higherly_ranked_perceptual_invocations(ranking)
            self.print("relevant invocations: %s" % (str(relevant_invocations)))
            for invocation in relevant_invocations:
                self.print("checking percept: %s" % (str(invocation)))
                # check whether indeed the trigger is the case
                percept_query = self.build_query(invocation)
                if percept_query():
                    self.print("percept confirmed. checking applicability.")
                    # look for the first applicable rule
                    rule = self.find_applicable_rule(invocation)
                    if rule is not None:
                        self.print("applicability confirmed, starting thread.")
                        # switching of thread
                        ranking = self.get_ranking(rule)  # taking the ranking of the new trigger
                        self.intentional_stack = []  # reset intentional stack
                        thread = self.append_thread(rule, ranking)  # creating and appending a new thread
                        self.print("intentional stack: %s " % str(self.intentional_stack))
                        break
        self.print("leaving kernel mode..")

        self.user_mode()

    def user_mode(self):
        self.print("entering in user mode..")

        thread, ranking = self.current_thread_ranking()

        if thread is not None:
            if thread.locked:
                if self.received(thread.unlocking_message):
                    thread.run()
                elif self.received(thread.timeout_message):
                    thread.fail()
            else:
                thread.run()
                if thread.locked is False:  # if the thread has been completed
                    self.kernel_mode()

        self.print("leaving user mode..")

    def current_thread_ranking(self):
        thread = self.intentional_stack[-1] if len(self.intentional_stack) > 0 else None
        ranking = thread.ranking if thread is not None else None
        return thread, ranking

    def daemon_step(self):

        print("%s >>> %s" % (self.body.name, self.intentional_stack))

        self.print(">>>>>>>>>>>>>> new decision cycle")

        self.print("intentional stack: %s" % self.intentional_stack)

        self.kernel_mode()

        self.print("<<<<<<<<<<<<<< end decision cycle")
