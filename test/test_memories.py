import unittest
from common.memories import Database
from common.messages import Commitment

class TestCase(unittest.TestCase):

    def test(self):
        base = Database()
        base.add(Commitment("raining"))
        base.add(Commitment("~raining"))
        base.add(Commitment("dog", {"name": "fido"}))
        base.add(Commitment("dog", {"name": "argo"}))
        assert len(base.tables) == 3
        assert len(base.tables["dog"].pos_data) == 2
        base.remove(Commitment("~raining"))
        assert len(base.tables) == 2
        assert len(base.tables["dog"].pos_data) == 2
        base.remove(Commitment("dog", {"name": "argo"}))
        assert len(base.tables) == 2
        assert len(base.tables["dog"].pos_data) == 1
