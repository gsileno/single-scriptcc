from enum import Enum


class Commitment:
    """A [generic] commitment is specified by a functor and parameters."""

    def __init__(self, functor, params=()):
        self.functor = functor
        self.params = params

    def is_atomic(self):
        return len(self.params) == 0

    def __str__(self):
        if len(self.params) == 0:
            return "%s" % self.functor
        else:
            return "%s(%s)" % (self.functor, str(self.params))

    def __repr__(self):
        return self.__str__()

    # TODO: it can be grounded and abstract


class CommitmentWithStrength(Commitment):
    """A [generic] commitment can be extended with a strength"""

    def __init__(self, strength, functor, params=()):
        super().__init__(functor, params)
        self.strength = strength

    def __str__(self):
        return "%s [%s]" % (super().__str__(), str(self.strength))


class SpeechActForce(Enum):
    ASSERTION = 1  # belief [epistemic commitment upon self]
    DIRECTIVE = 2  # expectation of action [practical commitment upon other]
    QUERY = 3  # expectation of belief [epistemic commitment upon other]
    PROMISE = 4  # action [practical commitment upon self]


class Reference(Commitment):
    def __init__(self, speech_act_force, functor, params=()):
        super().__init__(functor, params)
        self.force = speech_act_force

    def __str__(self):
        return "%s: %s" % (str(self.force), super().__str__())

    def to_assertion(self):
        return Reference(SpeechActForce.ASSERTION, self.functor, self.params)


class ReferenceWithStrength(Reference, CommitmentWithStrength):
    def __init__(self, speech_act_force, strength, functor, params=()):
        CommitmentWithStrength.__init__(self, strength, functor, params)
        self.force = speech_act_force

    def __str__(self):
        return "%s: %s" % (str(self.force), CommitmentWithStrength.__str__(self))


class Belief(Reference):
    def __init__(self, functor, params=()):
        super().__init__(SpeechActForce.ASSERTION, functor, params)


class BeliefWithStrength(ReferenceWithStrength):
    def __init__(self, strength, functor, params=()):
        super().__init__(SpeechActForce.ASSERTION, strength, functor, params)


class Desire(Reference):
    def __init__(self, functor, params=()):
        super().__init__(SpeechActForce.PROMISE, functor, params)


class DesireWithStrength(ReferenceWithStrength):
    def __init__(self, strength, functor, params=()):
        super().__init__(SpeechActForce.PROMISE, strength, functor, params)


class Command(Reference):
    def __init__(self, functor, params=()):
        super().__init__(SpeechActForce.DIRECTIVE, functor, params)


class CommandWithStrength(ReferenceWithStrength):
    def __init__(self, strength, functor, params=()):
        super().__init__(SpeechActForce.DIRECTIVE, strength, functor, params)


class Message:
    def __init__(self, reference, sender, receiver):
        self.content = reference
        self.sender = sender
        self.receiver = receiver
