import itertools

def remove_first_level(tree):
    tree_res = []
    for node in tree:
        if isinstance(node, list):
            tree_res.extend([i for i in node])
    return tree_res


def test_flatten():
    assert remove_first_level([]) == []
    assert remove_first_level([1, 100, 3]) == []
    assert remove_first_level([
        [1, [3, 2]],
        2,
        [3, 5],
        2,
        [130, [1, [550, 10]]],
    ]) == [1, [3, 2], 3, 5, 130, [1, [550, 10]]]