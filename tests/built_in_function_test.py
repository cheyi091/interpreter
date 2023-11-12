
def test_module(eva):
    
    # Math
    assert eva.eval(['+', 1, 5]) == 6
    assert eva.eval(['+', ['+', 3, 2], 5]) == 10
    assert eva.eval(['+', ['*', 3, 2], 5]) == 11

    # Comparison
    assert eva.eval(['>', 1, 5]) == False
    assert eva.eval(['<', 1, 5]) == True

    assert eva.eval(['>=', 5, 5]) == True
    assert eva.eval(['<=', 5, 5]) == True
    assert eva.eval(['=', 5, 5]) == True
    
