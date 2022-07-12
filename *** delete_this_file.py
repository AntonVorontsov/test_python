from math import *
import math

def make_segment(point1, point2):
    return {"begin_point": point1, "end_point": point2}


def get_begin_point(segment):
    return segment["begin_point"]


def get_end_point(segment):
    return segment["end_point"]


def is_parallel_with_x(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    return get_y(begin_point) == get_y(end_point)


def is_parallel_with_y(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    return get_x(begin_point) == get_x(end_point)


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }

x = 4
y = 8

point_1 = make_point(x, y)


def get_x(point):
    return int(point.get('radius') * cos(point.get('angle')))

print(get_x(point_1))


def get_y(point):
    return int(point.get('radius') * sin(point.get('angle')))

print(get_y(point_1))