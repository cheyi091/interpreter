
def test_module(eva):
    
    assert eva.eval(
        ['begin',
            ['var', 'result', 0],

            ['for', ['var', 'i', 0], ['<', 'i', 5], ['set', 'i', ['+', 'i', 1]],
                ['set', 'result', ['+', 'result', 'i']]
            ],

            'result'

        
        ]) == 10
