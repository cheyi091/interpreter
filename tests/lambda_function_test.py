
def test_module(eva):
    
    assert eva.eval(
        ['begin',
            ['def', 'on_click', ['callback'],
                ['begin', 
                    ['var', 'x', 10],
                    ['var', 'y', 20],
                    ['callback', ['+', 'x', 'y']],
                ]
            ],

            ['on_click', ['lambda', ['data'], ['*', 'data', 10]]]

        ]) == 300

    # Immediately-invoked lambda expression - IILE
    assert eva.eval(
        [['lambda', ['x'], ['*', 'x', 'x']], 2]) == 4

    # Save lambda to a variable
    assert eva.eval(
        ['begin',
            ['var', 'square', ['lambda', ['x'], ['*', 'x', 'x']]],

            ['square', 2]
        ]) == 4


    
