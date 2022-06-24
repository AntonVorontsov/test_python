def is_int(x):
    return isinstance(x, int)

def each2d(test, matrix):
    return all(all(test(cell) for cell in row) for row in matrix)

def some2d(test, matrix):
    return any(any(test(cell) for cell in row) for row in matrix)

def sum2d(test, matrix):
    return sum(sum(cell for cell in row if test(cell)) for row in matrix)
