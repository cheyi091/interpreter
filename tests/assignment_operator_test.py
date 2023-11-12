
def test_module(eva):
    
    assert eva.eval(
        ['begin',
            
            ['var', 'x', 0],

            ['++', 'x'],

            'x'
        
        ]) == 1
    
    assert eva.eval(
        ['begin',
            
            ['var', 'x', 0],

            ['--', 'x'],

            'x'
        
        ]) == -1
    
    assert eva.eval(
        ['begin',
            
            ['var', 'x', 0],

            ['+=', 'x', 5],

            'x'
        
        ]) == 5
    
    assert eva.eval(
        ['begin',
            
            ['var', 'x', 0],

            ['-=', 'x', 8],

            'x'
        
        ]) == -8
    
    assert eva.eval(
        ['begin',
            
            ['var', 'x', 2],

            ['*=', 'x', 3],

            'x'
        
        ]) == 6
    
    assert eva.eval(
        ['begin',
            
            ['var', 'x', 15],

            ['/=', 'x', 3],

            'x'
        
        ]) == 5

