
def test_module(eva):
    # Math:
    assert eva.eval(['+', 1, 5]) == 6
    assert eva.eval(['+', ['+', 3, 2], 5]) == 10
    assert eva.eval(['+', ['*', 3, 2], 5]) == 11
