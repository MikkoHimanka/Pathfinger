from math import sqrt


def distance(point_a, point_b):
    result = sqrt(
        abs(point_a[0] - point_b[0]) ** 2 + abs(point_a[1] - point_b[1])
    )

    return result
