def my_map(f, xs):
    result = []
    for i in xs:
        result = f(i)
        yield result


def my_filter(f, xs):
    for i in xs:
        if f(i) is True:
            yield i


def replicate_each(n, xs):
    for i in xs:
        a = 0
        while a < n:
            yield i
            a += 1
