from functions import get_function

without = get_function()


def test_without():
    assert without([2, 1, 2, 3, 4], 2, 3) == [1, 4]
    assert without([], 2) == []
