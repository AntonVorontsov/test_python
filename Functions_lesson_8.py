from operator import add, mul, sub


def greet(name, surname):
    return f'Hello, {name} {surname}!'


def adder(a, b):
    return a + b


def partial_apply(func, arg_1):
    def inner(arg_2):
        return(func(arg_1, arg_2))

    return inner


a = partial_apply(greet, 'Dorian')
print(a('Grey'))


def flip(func):
    def inner(arg_1, arg_2):
        return(func(arg_2, arg_1))

    return inner


f = flip(greet)
print(f('Dorian', 'Grey'))

n = list(
        map(partial_apply(add, 10), [1, 2, 3]),
    )

print(n)
