
def test_module(eva):
    
    assert eva.eval(
        ['begin',
            ['def', 'square', ['x'],
                ['*', 'x', 'x']
            ],
            
            ['square', 2]
        
        ]) == 4
    
    # Complex body
    assert eva.eval(
        ['begin',
            ['def', 'calc', ['x', 'y'],
                ['begin',
                    ['var', 'z', 30],
                    ['+', ['*', 'x', 'y'], 'z'],
                ]
            ],
            
            ['calc', 10, 20]
        
        ]) == 230

    # Closure
    assert eva.eval(
        ['begin',
            ['var', 'value', 100],

            ['def', 'calc', ['x', 'y'],
                ['begin',
                    ['var', 'z', ['+', 'x', 'y']],

                    ['def', 'inner', ['foo'],
                        ['+', ['+', 'foo', 'z'], 'value']
                    ],

                    'inner'
                ]
            ],
            
            ['var', 'fn', ['calc', 10, 20]],

            ['fn', 30]
        
        ]) == 160
    
