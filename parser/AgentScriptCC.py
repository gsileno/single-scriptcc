#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


####################
# --- Literals --- #
####################


class PosLiteral:

    def __init__(self, functor, terms=()):
        self.functor = functor
        self.terms = terms

    def __str__(self):
        output = self.functor
        if self.terms != ():
            output += "("
            for t in self.terms:
                output += str(t) + ", "
            output = output[:-2]
            output += ")"
        return output

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(self))

    def is_propositional(self):
        return len(self.terms) == 0

    def is_unary(self):
        return len(self.terms) == 1

    def is_abstract(self):
        return self.pos_literal.is_abstract()

    def is_grounded(self):
        return not self.is_abstract()


class NegLiteral:

    def __init__(self, pos_literal, neg):
        self.pos_literal = pos_literal
        self.neg = neg

    def __str__(self):
        if self.neg:
            prefix = "~"
        else:
            prefix = ""
        return prefix + str(self.pos_literal)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(self))

    def dual(self):
        return NegLiteral(self.pos_literal, not self.neg)

    def is_propositional(self):
        return self.pos_literal.is_propositional()

    def is_unary(self):
        return self.pos_literal.is_unary()

    def is_abstract(self):
        return self.pos_literal.is_abstract()

    def is_grounded(self):
        return not self.is_abstract()



#######################
# --- Expressions --- #
#######################


class Operator(Enum):
    AND = 1
    XOR = 2
    OR = 3
    POW = 4
    MULTIPLY = 5
    DIVIDE = 6
    MODULO = 7
    PLUS = 8
    MINUS = 9
    EQUAL = 10
    NOTEQUAL = 11
    LESS = 12
    LESSEQUAL = 13
    GREATER = 14
    GREATEREQUAL = 15

    @classmethod
    def from_text(cls, string):
        switcher = {
            "<": Operator.LESS,
            "<=": Operator.LESSEQUAL,
            ">=": Operator.GREATEREQUAL,
            ">": Operator.GREATER,
            "==": Operator.EQUAL,
            "!=": Operator.NOTEQUAL,
            "**": Operator.POW,
            "*": Operator.MULTIPLY,
            "/": Operator.DIVIDE,
            "%": Operator.MODULO,
            "mod": Operator.MODULO
        }

        return switcher[string]


class Expression:
    pass


class BinaryExpression(Expression):
    def __init__(self, operator, left_term, right_term):
        self.operator = operator
        self.left_term = left_term
        self.right_term = right_term

    def __str__(self):
        return "(%s %s %s)" % (str(self.left_term), str(self.operator), str(self.right_term))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(self))


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class Variable(Expression):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return str(self.identifier)

    def __repr__(self):
        return str(self)


#############################
# --- Beliefs and Goals --- #
#############################


class MentalAttitude:
    def __init__(self, content):
        self.content = content

    def is_propositional(self):
        return self.content.is_propositional()

    def is_unary(self):
        return self.content.is_unary()

    def is_abstract(self):
        return self.content.is_abstract()

    def is_grounded(self):
        return not self.is_abstract()


class Belief(MentalAttitude):
    def __str__(self):
        return str(self.content)


class TestGoal(MentalAttitude):
    def __str__(self):
        return "?" + str(self.content)


class ProceduralGoal(MentalAttitude):
    def __str__(self):
        return "!@" + str(self.content)


class AchievementGoal(MentalAttitude):
    def __str__(self):
        return "!" + str(self.content)


class MaintenanceGoal(MentalAttitude):
    def __str__(self):
        return "!!" + str(self.content)


class ExtMentalAttitude():
    def __init__(self, attitude, naf=False):
        self.attitude = attitude
        self.naf = naf

    def __str__(self):
        prefix = "not " if self.naf else ""
        return prefix + str(self.attitude)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return str(self)

    def nullify(self):
        return ExtMentalAttitude(self.attitude, True)

    def is_propositional(self):
        return self.attitude.is_propositional()

    def is_unary(self):
        return self.attitude.is_unary()


##########################
# --- Events/Actions --- #
##########################


class Event:
    def __init__(self, attitude, production=True):
        self.attitude = attitude
        self.production = production

    def __str__(self):
        prefix = "+" if self.production else "-"
        return prefix + str(self.attitude)

    def __repr__(self):
        return str(self)


class Action:
    pass


class InternalAction(Action, Event):
    pass


class PrimitiveAction(Action):
    def __init__(self, functor, params):
        self.functor = functor
        self.params = params

    def __str__(self):
        return self.functor  # TODO

    def __repr__(self):
        return str(self)


#################
# --- Rules --- #
#################


class TransformationalRule:

    def __init__(self, head=None, body=None):
        self.head = head
        self.body = body

    def __str__(self):
        return "{'body': " + str(self.body) + ", 'head': " + str(self.head) + "}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(self))

    def is_constraint(self):
        return self.head is None and self.body is not None

    def is_rule(self):
        return self.head is not None and self.body is not None


class ActiveRule:

    def __init__(self, event=None, condition=None, action=None):
        self.event = event
        self.conditions = condition
        self.action = action

    def __str__(self):
        return "{'event': " + str(self.event) + ", 'conditions': " + str(self.conditions) + ", 'actions': " + str(
            self.action) + "}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(self))


###################
# --- Program --- #
###################


class Program:
    def __init__(self, parsing_errors=None):
        self.parsing_errors = parsing_errors
        self.initial_attitudes = []
        self.transformational_rules = []
        self.active_rules = []

    def __str__(self):
        output = ""
        if len(self.initial_attitudes) > 0:
            output += "===========================\nInitial beliefs/goals:\n===========================\n"
            for instruction in self.initial_attitudes:
                output += str(instruction) + "\n"
            output += "\n"
        if len(self.transformational_rules) > 0:
            output += "===========================\nTransformational rules:\n===========================\n"
            for instruction in self.transformational_rules:
                output += str(instruction) + "\n"
            output += "\n"
        if len(self.active_rules) > 0:
            output += "===========================\nActive rules:\n===========================\n"
            for instruction in self.active_rules:
                output += str(instruction) + "\n"
            output += "\n"
        return output
