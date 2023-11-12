
# AST Transformer
class Transformer:
    def transform_def_to_var_lambda(self, def_exp):
        """
        Translate def-expression (function declaration)
        into a variable declaration with a lambda
        expression
        """
        _tag, name, params, body = def_exp
        return ['var', name, ['lambda', params, body]]
    
    def transform_from_switch_to_if(self, switch_exp):
        """
        Transform switch to nested if-expressions
        """
        _tag, *cases = switch_exp

        if_exp = ['if', None, None, None]

        current = if_exp
        
        for i in range(len(cases) - 1):
            current_cond, current_block = cases[i]
            current[1] = current_cond
            current[2] = current_block

            next_cond, next_block = cases[i+1]
            
            if next_cond == 'else':
                current[3] = next_block
            else:
                current[3] = ['if', None, None, None]

            current = current[3]
            
        return if_exp

    def transform_from_for_to_while(self, for_exp):
        """
        Transform for to while
        """
        _tag, initialize, condition, modifier, exp = for_exp
        return ['begin', initialize, ['while', condition, ['begin', exp, modifier]]]
    
    def transform_from_inc_to_set(self, inc_exp):
        """
        Transform increment to set
        """
        _tag, exp = inc_exp;
        return ['set', exp, ['+', exp, 1]];
    
    def transform_from_dec_to_set(self, dec_exp):
        """
        Transform decrement to set
        """
        _tag, exp = dec_exp;
        return ['set', exp, ['-', exp, 1]];

    def transform_from_inc_val_to_set(self, inc_val_exp):
        """
        Transform increment value to set
        """
        _tag, exp, val = inc_val_exp;
        return ['set', exp, ['+', exp, val]];
    
    def transform_from_dec_val_to_set(self, dec_val_exp):
        """
        Transform decrement vallue to set
        """
        _tag, exp, val = dec_val_exp;
        return ['set', exp, ['-', exp, val]];
    
    def transform_from_mul_val_to_set(self, mul_val_exp):
        """
        Transform multiply value to set
        """
        _tag, exp, val = mul_val_exp;
        return ['set', exp, ['*', exp, val]];
    
    def transform_from_div_val_to_set(self, div_val_exp):
        """
        Transform divide vallue to set
        """
        _tag, exp, val = div_val_exp;
        return ['set', exp, ['/', exp, val]];
