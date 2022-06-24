import operator
from operator import getitem
from functools import reduce
from operator import add

FALSES = (False, (), None, '', 0)
TRUTHS = (True, (1,), '!', -5)


def keep_truthful(items):
    A = filter(operator.truth, items)
    return list(A)


print(keep_truthful(TRUTHS))


def abs_sum(items):
    B = []
    for item in items:
        B.append(abs(item))
    return reduce(add, B)


SUM_ITEMS = [-3, -2, -1, 0, 1, 2, 3]

print(abs_sum(SUM_ITEMS))

city = {
    'Pine': {
        '5': 'School #42',
    },
    'Elm': {
        '13': {
            '1': 'Appartments #2, Elm st.13',
        },
    },
}

city_2 = {'a': {7: {'b': 42}}}

address = ['Pine', '5']
address_2 = ['Elm', '13', '1']
address_3 = ["a", 7, "b"]


def walk(addr, items):
    return reduce(getitem, addr, items)


print(walk(address_3, city_2))
