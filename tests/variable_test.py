
def test_module(eva):
    # Variables:
    assert eva.eval(['var', 'x', 10]) == 10
    assert eva.eval('x') == 10

    assert eva.eval(['var', 'y', 100]) == 100
    assert eva.eval('y') == 100

    assert eva.eval('VERSION') == '0.1'

    assert eva.eval(['var', 'isUser', 'true']) == True

    assert eva.eval(['var', 'z', ['*', 2, 2]]) == 4
    assert eva.eval('z') == 4
