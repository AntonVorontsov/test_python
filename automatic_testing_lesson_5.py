from validators import get_validator

# Такие штуки правильно делать через фикстуры.
# В следущих уроках мы разберём это подробнее.
make_validator = get_validator()


def test_validator():
    add_check, is_valid = make_validator()
    assert is_valid("value")
# BEGIN (write your solution here)
    add_check(lambda x: x > 5)
    add_check(lambda x: x % 2 == 0)
    assert is_valid(3) == False
    assert is_valid(4) == False
    assert is_valid(7) == False
    assert is_valid(8) == True

# END
