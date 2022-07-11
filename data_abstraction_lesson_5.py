from points import get_x, get_y, make_decart_point


# BEGIN (write your solution here)

def make_segment(point1, point2):
    return {"begin_point": point1, "end_point": point2}


def get_mid_point_of_segment(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    x = (get_x(begin_point) + get_x(end_point)) / 2
    y = (get_y(begin_point) + get_y(end_point)) / 2

    return make_decart_point(x, y)


def get_begin_point(segment):
    return segment["begin_point"]


def get_end_point(segment):
    return segment["end_point"]

# END