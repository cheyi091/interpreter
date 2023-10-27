
def test_module(eva):
    assert eva.eval(1) == 1
    assert eva.eval('"hello"') == 'hello'
