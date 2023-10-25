import re
from env import Environment

class Eva:
    def __init__(self, env=None):
        if env is None:
            env = Environment()
        self.env = env

    def eval(self, exp, env=None):
        if env is None:
            env = self.env

        # -------------------------------
        # Self-evaluating expressions:
        if self._is_number(exp):
            return exp
        
        if self._is_string(exp):
            return exp[1:-1]

        # -------------------------------
        # Math operations:
        if exp[0] == '+':
            return self.eval(exp[1]) + self.eval(exp[2])
        
        if exp[0] == '*':
            return self.eval(exp[1]) * self.eval(exp[2])
        
        # -------------------------------
        # Block: sequence of expressions:
        if exp[0] == 'begin':
            block_env = Environment()
            return self._eval_block(exp, env)

        # -------------------------------
        # Variable declaration:
        if exp[0] == 'var':
            _, name, value = exp
            return env.define(name, self.eval(value))
        
        # -------------------------------
        # Variable access:
        if self._is_variable_name(exp):
            return self.env.lookup(exp)

        raise Exception('Unimplemented')

    def _is_number(self, exp):
        return isinstance(exp, (int, float))

    def _is_string(self, exp):
        return isinstance(exp, str) and exp.startswith('"') and exp.endswith('"')
    
    def _is_variable_name(self, exp):
        return isinstance(exp, str) and re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', exp) is not None

    def _eval_block(self, block, env):
        _tag, *expressions = block
        for exp in expressions:
            result = self.eval(exp, env)
        return result


# Tests:
eva = Eva(Environment({
    'null': None,
    'true': True,
    'false': False,
    'VERSION': '0.1',
    }))

# Math:
assert eva.eval(1) == 1
assert eva.eval('"hello"') == 'hello'
assert eva.eval(['+', 1, 5]) == 6
assert eva.eval(['+', ['+', 3, 2], 5]) == 10
assert eva.eval(['+', ['*', 3, 2], 5]) == 11

# Variables:
assert eva.eval(['var', 'x', 10]) == 10
assert eva.eval('x') == 10

assert eva.eval(['var', 'y', 100]) == 100
assert eva.eval('y') == 100

assert eva.eval('VERSION') == '0.1'

assert eva.eval(['var', 'isUser', 'true']) == True

assert eva.eval(['var', 'z', ['*', 2, 2]]) == 4
assert eva.eval('z') == 4

# Blocks
assert eva.eval(
    ['begin',
        ['var', 'x', 10],
        ['var', 'y', 20],

        ['+', ['*', 'x', 'y'], 30],

    ]) == 230

assert eva.eval(
    ['begin',
        ['var', 'x', 10],
        
        ['begin',
            ['var', 'x', 20],
            'x'
        
        ],

        'x',

    ]) == 10



print('All assertions passed!')
