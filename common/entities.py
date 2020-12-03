class TimedEntity():
    """a timed entity has an internal timer, at each time step it triggers a daemon step"""

    def __init__(self):
        self.time = 0

    def run_time_step(self):
        self.time += 1
        self.run_step()

    def run_step(self):
        """function which is run at each execution cycle"""
        self.daemon_step()

    def daemon_step(self):
        """this should contain the core controller process"""
        pass



class PassiveEntity(TimedEntity):
    """an environment is a reactive and timed entity. it may contain independent active entities"""

    def __init__(self, name, init_params=None):
        """an environment has possibly some initiating parameters"""

        TimedEntity.__init__(self)

        self.name = name
        self.active_entities = {}

        if init_params is not None:
            for key in init_params.keys():
                if hasattr(self, key):
                    self.key = init_params[key]
                else:
                    raise RuntimeError("Unknown parameter \"%s\"." % (str(key)))

    def get_state(self):
        """return the state of the environment as a dict"""
        return vars(self)

    def get_factors(self):
        """return the factors/features defining the state of the environment"""
        l = list(vars(self).keys())
        l.remove("time")
        l.remove("name")
        l.remove("active_entities")
        return tuple(l)

    def register_active_entity(self, name, type, init_params=None):
        """create a body of a certain type in the environment, possibly initiated with some parameters"""
        if not issubclass(type, ActiveEntity):
            raise TypeError("\"%s\" is not a valid ActiveEntity type." % (type))

        if name in self.active_entities:
            raise RuntimeError("An ActiveEntity with id \"%s\" has been already registered." % (name))

        entity = type(self, name, init_params)
        self.active_entities[name] = entity

        return entity

    def run_step(self):
        """passive entities first run their own controller and then triggers their controlled entities"""
        self.daemon_step()

        for entity in self.active_entities.values():
            entity.run_time_step()



class Process:
    def __init__(self, mechanism, callback=None, duration=0):
        self.mechanism = mechanism
        self.callback = callback
        self.duration = duration

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(self))



class ActiveEntity(PassiveEntity):
    """active entities are associated to an enviroment, and possibly by and a single thread"""

    def __init__(self, environment, name, init_params=None):
        if not isinstance(environment, PassiveEntity):
            raise RuntimeError("\"%s\" is not a valid Environment." % (environment))

        self.environment = environment
        self.running_process = None

        PassiveEntity.__init__(self, name, init_params)

    def get_primitives(self):
        """return all primitive actions (methods) for this body-type"""
        return [f for f in dir(type(self)) if callable(getattr(type(self), f)) \
                and not f.startswith('__') and not str(f) in
                                                   ['get_primitives', 'get_state', 'get_factors', 'daemon_step',
                                                    'perceive', 'send_message', 'push', 'pop', 'received', 'flush',
                                                    'initiate_process', 'register_active_entity', 'print',
                                                    'remove_process', 'run_time_step', 'run_step', 'simulate_process']]

    def get_factors(self):
        """return the factors/features defining the (external) state of the body"""
        l = list(super().get_factors())
        l.remove("environment")
        l.remove("running_process")
        return tuple(l)

    def initiate_process(self, process, callback=None, duration=0):
        if self.running_process is not None:
            raise Warning("There was a running process now (%s)." % (str(self.running_process)))
        else:
            if process not in self.get_primitives():
                raise Warning("Undefined process (%s) in primitives (%s)." % (process, str(self.get_primitives())))
            else:
                self.running_process = Process(process, callback, duration)

    def remove_process(self):
        if self.running_process is None:
            raise Warning("There was no running process now.")
        else:
            self.running_process = None

    def simulate_process(self):
        if self.running_process is not None:
            self.running_process.duration -= 1
            if self.running_process.duration < 0:
                f = getattr(self, self.running_process.mechanism)
                callback = self.running_process.callback
                self.running_process = None
                f()
                print(callback)
                if callback is not None:
                    callback()

    def run_step(self):
        """active entities first run their own controller, then the ancillary process, then triggers their controlled entities (if any)"""
        self.daemon_step()

        if self.running_process is not None:
            self.simulate_process()

        for entity in self.active_entities.values():
            entity.run_time_step()
