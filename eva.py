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
        # Block: sequence of expressions:
        if exp[0] == 'begin':
            block_env = Environment(parent=env)
            return self._eval_block(exp, block_env)

        # -------------------------------
        # Variable declaration: (var foo 10)
        if exp[0] == 'var':
            _, name, value = exp
            return env.define(name, self.eval(value, env))
        
        # -------------------------------
        # Variable update: (set foo 10)
        if exp[0] == 'set':
            _, name, value = exp
            return env.assign(name, self.eval(value, env))
        
        # -------------------------------
        # Variable access: foo
        if self._is_variable_name(exp):
            return env.lookup(exp)
        
        # -------------------------------
        # if-expression
        if exp[0] == 'if':
            _tag, condition, conseqeunt, alternate = exp
            if self.eval(condition):
                return self.eval(consequent, env)
            return  self.eval(alternate, env)
        
        # -------------------------------
        # while-expression
        if exp[0] == 'while':
            _tag, condition, body = exp
            while self.eval(condition, env):
                result = self.eval(body, env)
            return result

        # -------------------------------
        # Function calls:
        #
        # (print "Hello World")
        # (+ x 5)
        # (> foo bar)
        if isinstance(exp, list):
            fn = self.eval(exp[0], env)

            args = [self.eval(arg, env) for arg in exp[1:]]  # Equivalent to map(this.eval, arg, env)

            if callable(fn):
                return fn(*args)



        raise Exception('Unimplemented')

    def _is_number(self, exp):
        return isinstance(exp, (int, float))

    def _is_string(self, exp):
        return isinstance(exp, str) and exp.startswith('"') and exp.endswith('"')
    
    def _is_variable_name(self, exp):
        #return isinstance(exp, str) and re.match(r'^[+*/\-=<>a-zA-Z][a-zA-Z0-9_]*$', exp) is not None
        return isinstance(exp, str) and re.match(r'^[+*/\-=<>a-zA-Z0-9_]*$', exp) is not None

    def _eval_block(self, block, env):
        _tag, *expressions = block
        for exp in expressions:
            result = self.eval(exp, env)
        return result


def run_tests(env):
    from tests import self_eval_test
    from tests import math_test
    from tests import variable_test
    from tests import block_test
    from tests import if_test
    from tests import while_test
    from tests import built_in_function_test

    eva = Eva(env)

    # List of tests
    tests = [
             self_eval_test.test_module, 
             math_test.test_module, 
             variable_test.test_module, 
             block_test.test_module, 
             if_test.test_module, 
             while_test.test_module,
             built_in_function_test.test_module,
            ]

    # Execute each test
    for test_function in tests:
        test_function(eva)

    eva.eval(['print', '"Hello"', '"World"'])

    print("All assertions passed!")


if __name__ == '__main__':
    env = Environment({
        'null': None,

        'true': True,
        'false': False,
        
        'VERSION': '0.1',
            
        # Operators
        '+': lambda op1, op2: op1 + op2,
        '*': lambda op1, op2: op1 * op2,
        '-': lambda op1, op2=None: -op1 if op2 is None else op1 - op2,
        '/': lambda op1, op2: op1 / op2,
        
        # Comparison
        '>': lambda op1, op2: op1 > op2,
        '>=': lambda op1, op2: op1 >= op2,
        '<': lambda op1, op2: op1 < op2,
        '<=': lambda op1, op2: op1 <= op2,
        '=': lambda op1, op2: op1 == op2,

        'print': lambda *args: print(*args),

    })

    run_tests(env)
