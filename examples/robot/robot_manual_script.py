"""
BDI agent execution model, manual coding
python version of robot.ascript
single thread, hard-coded control flow
"""

from common.agency import *


class RobotBeliefsBase(EmbodiedDatabase):

    # propositional predicates

    def near_door(self): return self.body.perceive("near_door")
    def near_plug(self): return self.body.perceive("near_plug")
    def fresh(self): T = self.get_temp(); return T < 40
    def veryhot(self): T = self.get_temp(); return T > 70
    def uncharged(self): T = self.get_temp(); return T < 20

    # unary predicates

    def temp(self, T): return T == self.get_temp()
    def get_temp(self): return self.body.perceive("temp")

    # negation as failures

    def neg_fresh(self): return not self.fresh()
    def neg_veryhot(self): return not self.veryhot()
    def neg_uncharged(self): return not self.uncharged()
    def neg_temp(self, T): return not self.temp(T)


class RobotAgent(IntentionalAgent):

    def __init__(self, body):
        super().__init__(body, beliefsbase_type=RobotBeliefsBase)

    @classmethod
    def rule_to_conditions(cls):
        return {
            "!@open_1": [ "near_door" ],
            "!@charge_1": [ "near_plug" ]
        }

    @classmethod
    def rule_to_actions(cls):
        return {
            "veryhot": ["!~veryhot"],
            "uncharged": ["!~uncharged"],
            "~fresh": ["!fresh"],
            "!~veryhot": ["!@open"],
            "!fresh": ["!@open"],
            "!~uncharged": ["!@charge"],
            "!@open_1": ["#open_door"],
            "!@open_2": ["#go_door", "!@open_1"],
            "!@charge_1": ["#charge_battery"],
            "!@charge_2": ["#go_plug", "!@charge_1"]
        }

    @classmethod
    def rule_to_ranking(cls):
        return {
            "veryhot" : 0,
            "uncharged" : 1,
            "~fresh": 2,
            "!~veryhot": 3,
            "!fresh": 4,
            "!~uncharged": 5,
            "!@open_1": 6,
            "!@open_2": 7,
            "!@charge_1": 8,
            "!@charge_2": 9
        }

    @classmethod
    def goal_to_rules(cls):
        return {
            "!@open": ["!@open_1", "!@open_2"],
            "!@charge": ["!@charge_1", "!@charge_2"]
        }


if __name__ == "__main__":

    from examples.robot.robot_entities import RobotEnvironment
    environment = RobotEnvironment()
    robot_body = environment.register_active_entity("robot")
    robot_agent = RobotAgent(robot_body)

    for i in range(100):
        print("---------------------------------------------------------------------------------")
        print("time step: %d" % i)
        # environmental update
        environment.run_time_step()
        # decision-making cycle
        robot_agent.daemon_step()
