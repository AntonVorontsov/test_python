#from functools import lru_cache - стандартная библиотека python, реализующая поставленную в задании задачу

def memoized(function):
    cache = {}

    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = function(*args)
            return cache[args]
    return inner

@memoized
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
