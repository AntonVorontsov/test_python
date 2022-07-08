def fill(collection, value, begin=0, end=None):
    chunk = [value for _ in collection[begin:end]]
    collection[begin:end] = chunk
    return collection


coll = [1, 2, 3, 4]

print(fill(coll, '*', 1, 3))
