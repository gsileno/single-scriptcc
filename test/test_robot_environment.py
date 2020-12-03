import unittest
from examples.robot.robot_entities import RobotEnvironment


class TestCase(unittest.TestCase):

    def test(self):
        # create the environment
        env = RobotEnvironment()

        # check environmental factors and state
        env_factors = env.get_factors()
        assert len(env_factors) == 2
        env_state = env.get_state()
        assert len(env_state.keys()) == 5
        assert len(env_state["active_entities"]) == 0
        assert env_state["temp"] == 30

        # run a single time step
        env.run_time_step()

        # check changes to environment
        assert env_state["temp"] == 31

        # register an body to environment
        env.register_active_entity("robot")

        # check environmental state concering bodies
        assert len(env_state.keys()) == 5
        assert len(env_state["active_entities"]) == 1

        # check body factors, state and primitive actions
        robot = env_state["active_entities"]["robot"]
        robot_factors = robot.get_factors()
        assert len(robot_factors) == 4
        robot_state = robot.get_state()
        assert len(robot_state.keys()) == 9
        assert robot_state["battery"] == 70
        print(robot.get_primitives())
        assert len(robot.get_primitives()) == 4

        # run a single time step
        env.run_time_step()

        # check changes to environment and body
        assert env_state["temp"] == 32
        assert robot_state["battery"] == 69
        assert env_state["open_door"] == False
        assert robot_state["plugged"] == False

        # execute some action (without timing)
        assert robot.charge_battery() == False
        assert robot.open_door() == False
        assert robot_state["near_plug"] == False
        assert robot.go_plug() == True
        assert robot_state["near_plug"] == True
        assert robot.go_plug() == True
        assert robot.charge_battery() == True
        assert robot.open_door() == False
        assert robot_state["plugged"] == True

        # run a single time step
        env.run_time_step()

        # check changes to environment and body
        assert env_state["temp"] == 33
        assert robot_state["battery"] == 74

        # execute some action (without timing)
        assert robot.charge_battery() == True
        assert robot.open_door() == False
        assert env_state["open_door"] == False
        assert robot_state["plugged"] == True
        assert robot_state["near_door"] == False
        assert robot.go_door() == True
        assert robot_state["near_door"] == True
        assert robot.go_door() == True
        assert env_state["open_door"] == False
        assert robot_state["plugged"] == False
        assert robot.charge_battery() == False
        assert robot.open_door() == True
        assert env_state["open_door"] == True
        assert robot_state["plugged"] == False

        # run a single time step
        env.run_time_step()

        # check changes to environment and body
        assert env_state["temp"] == 32
        assert robot_state["battery"] == 73
