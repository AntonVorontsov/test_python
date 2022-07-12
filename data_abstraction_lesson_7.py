from points import get_quadrant, get_x, get_y, make_decart_point


# BEGIN (write your solution here)
def make_rectangle(start_point, width, height):
    return {
        "start_point": start_point,
        "width": width,
        "height": height,
    }


def get_start_point(rectangle):
    return rectangle["start_point"]


def get_width(rectangle):
    return rectangle["width"]


def get_height(rectangle):
    return rectangle["height"]


def get_ur_rectangle_point(rectangle):
    return make_decart_point(
        get_x(get_start_point(rectangle)) + get_width(rectangle),
        get_y(get_start_point(rectangle)),
    )


def get_dl_rectangle_point(rectangle):
    return make_decart_point(
        get_x(get_start_point(rectangle)),
        get_y(get_start_point(rectangle)) - get_height(rectangle),
    )


def get_dr_rectangle_point(rectangle):
    return make_decart_point(
        get_x(get_start_point(rectangle)) + get_width(rectangle),
        get_y(get_start_point(rectangle)) - get_height(rectangle),
    )


def contains_origin(rectangle):
    points_quadrants = (
        get_quadrant(get_start_point(rectangle)),
        get_quadrant(get_ur_rectangle_point(rectangle)),
        get_quadrant(get_dl_rectangle_point(rectangle)),
        get_quadrant(get_dr_rectangle_point(rectangle)),
    )
    return len(set(points_quadrants)) == 4

# END
