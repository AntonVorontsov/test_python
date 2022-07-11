def get_mid_point(p1, p2):
    x1 = p1.get('x')
    x2 = p2.get('x')
    y1 = p1.get('y')
    y2 = p2.get('y')

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return {'x': x, 'y': y}


point1 = {'x': -1, 'y': 10}
point2 = {'x': 0, 'y': -3}

print(get_mid_point(point1, point2))
