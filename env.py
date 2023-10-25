class Environment:
    def __init__(self, record=None, parent=None):
        if record == None:
            record = {}
        self.record = record
        self.parent = parent

    def define(self, name, value):
        """
        Creates a variable with the given name and value.
        """
        self.record[name] = value
        return value

    def lookup(self, name):
        """
        Returns the value of a defined variable, or throws
        if the variable is not defined
        """
        if name not in self.record:
            raise ReferenceError(f"Variable '{name}' not defined")
        return self.record[name]
