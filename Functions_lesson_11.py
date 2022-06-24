from functools import wraps


def memoizing(n):
    def memoized(function):
        cache = {}
        @wraps(function)

        def inner(*args):
            if args in cache:
                return cache[args]
            else:
                if len(cache) < n:
                    cache[args] = function(*args)
                    return cache[args]
                else:
                    cache.pop(list(cache)[0])
                    cache[args] = function(*args)
                    return cache[args]
        return inner
    return memoized


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10
