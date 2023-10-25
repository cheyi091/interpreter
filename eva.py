class Eva:
    def eval(self, exp):
        if self._is_umber(exp):
            return exp
        
        if self._is_string(exp):
            return exp[1:-1]

        if exp[0] == '+':
            return exp[1] + exp[2]
        
        raise Exception('Unimplemented')

    def _is_number(self, exp):
        return isinstance(exp, (int, float))

    def _is_string(self, exp):
        return isinstance(exp, str) and exp.startswith('"') and exp.endswith('"')


# Tests:
eva = Eva()

assert eva.eval(1) == 1
assert eva.eval('"hello"') == 'hello'
assert eva.eval(['+', 1, 5]) == 6
assert eva.eval(['+', ['+', 3, 2], 5]) == 10
