import math


# BEGIN (write your solution here)
def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return distance

# END
