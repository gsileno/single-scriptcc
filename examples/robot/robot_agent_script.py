# automatically generated with scriptcc -- 03 December 2020

from common.agency import IntentionalAgent

class Robot(IntentionalAgent):

    def __init__(self, body):
        super().__init__(body, beliefsbase_type=###BELIEFSBASECLASS###)

    @classmethod
    def rule_to_conditions(cls):
        return {
            "!@open_1": [ "near_door"],
            "!@charge_1": [ "near_plug"],
        }

    @classmethod
    def rule_to_actions(cls):
        return {
            "veryhot": [ "+!~veryhot"],
            "uncharged": [ "+!~uncharged"],
            "~fresh": [ "+!fresh"],
            "!~veryhot": [ "+!@open"],
            "!fresh": [ "+!@open"],
            "!~uncharged": [ "+!@charge"],
            "!@open_1": [ "open_door"],
            "!@open_2": [ "go_door",  "+!@open"],
            "!@charge_1": [ "charge_battery"],
            "!@charge_2": [ "go_plug",  "+!@charge"],
        }

    @classmethod
    def rule_to_ranking(cls):
        return {
            "veryhot": 0,
            "uncharged": 1,
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
            "!@open": [ "!@open_1",  "!@open_2"],
            "!@charge": [ "!@charge_1",  "!@charge_2"],
        }


