import math

def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return distance

point1 = [0, 0]
point2 = [3, 4]

print(calculate_distance(point1, point2))