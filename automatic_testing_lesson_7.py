from cart import get_implementations

make_cart = get_implementations()


# BEGIN (write your solution here)
cart = make_cart()
cart.add_item({'name': 'car', 'price': 3}, 5)
cart.add_item({'name': 'house', 'price': 10}, 2)
cart.add_item({'name': 'house', 'price': 10}, 1)


def test_get_items():
    assert len(cart.get_items()) == 3


def test_get_cost():
    assert cart.get_cost() == 45

# END


# Решение учителя

from cart import get_implementations

# make_cart = get_implementations()
#
#
# # BEGIN
# def test_cart():
#     cart = make_cart()
#     assert not len(cart.get_items())
#
#     cart.add_item({'name': 'car', 'price': 3}, 5)
#     assert len(cart.get_items()) == 1
#     assert cart.get_cost() == 15
#     assert cart.get_count() == 5
#
#     cart.add_item({'name': 'house', 'price': 10}, 2)
#     assert len(cart.get_items()) == 2
#     assert cart.get_cost() == 35
#     assert cart.get_count() == 7
# # END