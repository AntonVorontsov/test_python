def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None


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


p = make_decart_point(-4, 3)
rectangle1 = make_rectangle(p, 5, 4)
print(contains_origin(rectangle1))

rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
print(contains_origin(rectangle2))
