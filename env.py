class Environment:
    def __init__(self, record=None, parent=None):
        if record is None:
            record = {}
        self.record = record
        self.parent = parent

    def define(self, name, value):
        """
        Creates a variable with the given name and value.
        """
        self.record[name] = value
        return value

    def assign(self, name, value):
        """
        Updates an existing variable.
        """
        self.resolve(name).record[name] = value
        return value

    def lookup(self, name):
        """
        Returns the value of a defined variable, or throws
        if the variable is not defined
        """
        return self.resolve(name).record[name]

    def resolve(self, name):
        """
        Returns specific environment in which a variable is defined, or
        throws if a variable is not defined
        """
        #print(f'name: {name}')
        if name in self.record:
            return self
        if self.parent is None:
            raise ReferenceError(f'Variable "{name}" is not defined.')
        return self.parent.resolve(name)
