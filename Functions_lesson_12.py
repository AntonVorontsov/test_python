def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)


def is_odd(n):
    return not is_even(n)


#Решение учителя:
#
# def is_odd(number):
#     return False if number == 0 else is_even(number - 1)
#
#
# def is_even(number):
#     return True if number == 0 else is_odd(number - 1)
