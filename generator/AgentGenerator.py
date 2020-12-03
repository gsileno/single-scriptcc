from parser.AgentScriptCC import *


def generate_dict(dict):
    output = "        return {\n"
    with_list = False
    for key in dict.keys():
        if type(dict[key]) == list:
            with_list = True
            output += "            \"%s\": [" % (str(key))
            for value in dict[key]:
                output += " \"%s\", " % value
            output = output[:-2]
            output += "],\n"
        else:
            output += "            \"%s\": %s,\n" % (str(key), str(dict[key]))
    if with_list is False:
        output = output[:-2]+"\n"

    output += "        }\n\n"
    return output


class Generator:

    def __init__(self, name, program):
        self.name = name
        self.program = program

    def generate(self):

        rule_to_conditions = {}
        rule_to_actions = {}
        rule_to_ranking = {}
        goal_to_rules = {}
        goal_frequency = {}
        goal_frequency_counter = {}

        for rule in self.program.active_rules:
            if rule.event.production is False:
                raise RuntimeError("Not yet implemented")
            else:
                invocation = str(rule.event.attitude)
                if invocation in goal_frequency:
                    goal_frequency[invocation] += 1
                else:
                    goal_frequency[invocation] = 1
                    goal_frequency_counter[invocation] = 1

        ranking = 0
        for rule in self.program.active_rules:
            invocation = str(rule.event.attitude)
            if goal_frequency[invocation] > 1:
                label = "%s_%d" % (invocation, goal_frequency_counter[invocation])
                goal_frequency_counter[invocation] += 1

                if invocation in goal_to_rules:
                    goal_to_rules[invocation].append(label)
                else:
                    goal_to_rules[invocation] = [label]
            else:
                label = invocation

            rule_to_ranking[label] = ranking

            if rule.conditions is not None:
                if len(rule.conditions) == 1 and isinstance(rule.conditions[0], ExtMentalAttitude):
                    rule_to_conditions[label] = [str(rule.conditions[0])]
                else:
                    raise RuntimeError("Not yet implemented")

            rule_to_actions[label] = []
            for action in rule.action:
                rule_to_actions[label].append(str(action))

            ranking += 1

        from datetime import date
        output = "# automatically generated with scriptcc -- " + date.today().strftime("%d %B %Y") + "\n\n"
        output += "from common.agency import IntentionalAgent\n\n"

        output += "class %s(IntentionalAgent):\n\n" % self.name.capitalize()

        output += """    def __init__(self, body):
        super().__init__(body, beliefsbase_type=###BELIEFSBASECLASS###)\n\n"""

        # rule_to_conditions

        output += "    @classmethod\n"
        output += "    def rule_to_conditions(cls):\n"
        output += generate_dict(rule_to_conditions)

        # rule_to_actions

        output += "    @classmethod\n"
        output += "    def rule_to_actions(cls):\n"
        output += generate_dict(rule_to_actions)

        # rule_to_ranking

        output += "    @classmethod\n"
        output += "    def rule_to_ranking(cls):\n"
        output += generate_dict(rule_to_ranking)

        # goal_to_rules

        output += "    @classmethod\n"
        output += "    def goal_to_rules(cls):\n"
        output += generate_dict(goal_to_rules)

        return output
