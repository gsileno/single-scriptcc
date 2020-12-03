from common.entities import PassiveEntity, ActiveEntity


class RobotDefaultBody(ActiveEntity):
    """default robot body for the robot environment."""

    def __init__(self, environment, name, init_params=None):
        """a robot has a battery, can be nearby the door, nearby a plug and can be plugged."""

        ## default features (body-level)
        self.battery = 70
        self.near_door = False  # position of the body w.r.t. door
        self.near_plug = False  # position of the body w.r.t. door
        self.plugged = False

        super().__init__(environment, name, init_params)

    def print(self, text): print(self.name + " >>> " + text)

    def daemon_step(self):
        # if the robot is plugged it charges, otherwise it decharges
        if self.plugged is False:
            self.battery -= 1
            self.print("battery decreases to %d" % (self.battery))
        else:
            self.battery = min(self.battery + 5, 100)
            self.print("battery increases to %d" % (self.battery))

    ## primitive susceptibilities
    def perceive(self, target):
        if target == "near_door":
            return self.near_door
        elif target == "near_plug":
            return self.near_plug
        elif target == "temp":
            return self.environment.temp
        elif target == "battery":
            return self.battery
        else:
            raise RuntimeError("\"%s\" is a not known target for perception " % (target))

    ## primitive actions
    def open_door(self):
        if self.environment.open_door is True:
            self.print("door already open")
            return True

        self.print("attempt open door")
        if self.near_door:
            self.environment.open_door = True
            print("=> door open")
            return True
        else:
            return False

    def charge_battery(self):
        if self.plugged is True:
            self.print("already plugged")
            return True

        self.print("attempt charge battery")
        if self.near_plug:
            self.print("=> battery plugged")
            self.plugged = True
            return True
        else:
            return False

    def go_door(self):
        if self.near_door is True:
            self.print("already near door")
            return True

        self.print("go towards door (and by doing so taking out the plug)")
        self.near_door = True
        self.near_plug = False
        self.plugged = False
        return True

    def go_plug(self):
        if self.near_plug is True:
            self.print("already near plug")
            return True

        self.print("go towards plug")
        self.near_door = False
        self.near_plug = True
        return True


class RobotEnvironment(PassiveEntity):

    def __init__(self, init_params=None):

        ## features (environment-level)
        self.open_door = False
        self.temp = 30

        super().__init__(init_params)

    def daemon_step(self):
        # if no body is nearby the door, the door closes (immediately)
        some_body_near_door = False
        for body in self.active_entities.values():
            if body.near_door:
                some_body_near_door = True

        if not some_body_near_door:
            print("nobody holds the door. it is closed.")
            self.open_door = False

        # if the door is closed, the temperature raises
        if self.open_door is False:
            self.temp += 1
            print("temperature increases to %d" % (self.temp))
        else:
            self.temp -= 1
            print("temperature decreases to %d" % (self.temp))

    def register_active_entity(self, name, type=RobotDefaultBody, init_params=None):
        return super().register_active_entity(name, type, init_params)