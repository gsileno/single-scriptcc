import unittest
from common.entities import TimedEntity, PassiveEntity, ActiveEntity, Process
from common.agency import EntityWithMessageQueue

class TestActiveEntity(ActiveEntity):

    def __init__(self, environment, name, init_params=None):
        self.said_hello = False
        super().__init__(environment, name, init_params)

    def say_hello(self):
        self.said_hello = True


class TestCase(unittest.TestCase):

    def test00(self):
        e = EntityWithMessageQueue()
        e.push("test")
        assert len(e.queue) == 1
        o = e.pop()
        assert o == "test"
        assert len(e.queue) == 0

    def test01(self):
        e = EntityWithMessageQueue()
        f = EntityWithMessageQueue()
        e.push("test")
        assert len(e.queue) == 1
        assert len(f.queue) == 0
        e.send_message(f, "test2")
        assert len(e.queue) == 1
        assert len(f.queue) == 1
        assert e.pop() == "test"
        assert f.pop() == "test2"
        assert len(e.queue) == 0
        assert len(f.queue) == 0

    def test1(self):
        e = TimedEntity()
        for i in range(10):
            e.run_time_step()
            assert e.time == i + 1

    def test2(self):
        e = PassiveEntity("env")

    def test3(self):
        e = PassiveEntity("env")
        a = e.register_active_entity("agent0", ActiveEntity)
        assert len(a.get_primitives()) == 0
        a = e.register_active_entity("agent1", TestActiveEntity)
        assert len(a.get_primitives()) == 1
        a.initiate_process("say_hello", duration=10)
        assert a.running_process == Process("say_hello", duration=10)
        assert a.said_hello == False
        for i in range(9):
            e.run_time_step()
        assert a.running_process == Process("say_hello", duration=1)
        e.run_time_step()
        assert a.said_hello == False
        assert a.running_process == Process("say_hello", duration=0)
        e.run_time_step()
        assert a.said_hello == True
        assert a.running_process == None


if __name__ == '__main__':
    unittest.main()
