import math
from math import cos, sin


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


# BEGIN (write your solution here)
def get_x(point):
    return int(point.get('radius') * cos(point.get('angle')))


def get_y(point):
    return int(point.get('radius') * sin(point.get('angle')))

# END
