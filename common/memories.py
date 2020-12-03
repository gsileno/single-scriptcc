def matches(query, dict):
    for key in query.keys():
        if key not in dict:
            return None  # I assume here the absence of a field for an item means its absence
        if query[key] != dict[key]:
            return None
    return dict


class Table:
    def __init__(self):
        self.pos_data = {}
        self.pos_valence = {}
        self.pos_intensity = {}

    def find_data(self, query):
        for pos in self.pos_data.keys():
            if matches(query, self.pos_data[pos]):
                return pos, self.pos_data[pos], self.pos_valence[pos], self.pos_intensity[pos]
        return None, None, None, None

    def add_data(self, data, valence=True, intensity=1):
        if data is None:
            raise RuntimeError("You should not be here.")
        if intensity <= 0:
            raise RuntimeError("Intensities are expected to be >= 1")
        elif intensity < 1:
            intensity = 1 / intensity
            valence = not valence

        n = len(self.pos_data)
        self.pos_data[n] = data
        self.pos_valence[n] = valence
        self.pos_intensity[n] = intensity

    def remove_data(self, data):
        pos, _, _, _ = self.find_data(data)
        if pos is None:
            raise RuntimeError("data '%s' not found." % data)
        else:
            self.pos_data.pop(pos)


class Database:
    def __init__(self):
        self.tables = {}

    def add_table(self, name):
        if name in self.tables:
            raise RuntimeError("table '%s' already existing." % name)
        self.tables[name] = Table()

    def find(self, term):
        table_name = term.functor
        if table_name not in self.tables:
            return False
        return self.tables[table_name].find_data(term.params)

    def add(self, term, pos=True, strength=1):
        table_name = term.functor
        if table_name not in self.tables:
            self.add_table(table_name)

        if term.is_atomic():
            self.tables[table_name] = True
        else:
            self.tables[table_name].add_data(term.params, strength)

    def remove(self, term):
        table_name = term.functor
        if table_name not in self.tables:
            raise RuntimeError("Table '%s' does not exist." % table_name)
        if term.is_atomic():
            self.tables.pop(table_name)
        else:
            self.tables[table_name].remove_data(term.params)
            # TODO: should we remove the table if there is no data anymore?


class EmbodiedDatabase(Database):
    def __init__(self, body):
        super().__init__()
        self.body = body

    def get_primitives(self):
        """return all primitive inference (methods) for this body-type"""
        return (f for f in dir(type(self)) if callable(getattr(type(self), f)) \
                and not f.startswith('__') and not str(f) in \
                ['query', 'get_primitives', 'add_table', 'find', 'add', 'remove'])

    def query(self, term):
        """first look whether there is a procedure to compute the queried term, otherwise looks for existing matching items in the database"""
        if term.functor[0] == "~":
            table_name = "neg_"+term.functor[1:]
        else:
            table_name = term.functor
        primitives = self.get_primitives()
        if table_name in primitives:
            f = getattr(self, table_name)
            if term.is_atomic():
                return f()
            else:
                raise RuntimeError("To be implemented.")
                # return f(term.params)
        else:
            return self.find(term)
