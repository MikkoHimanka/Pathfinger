from math import sqrt


def distance(point_a, point_b):
    result = sqrt(
        (point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2
    )
    return result


def manhattan_distance(point_a, point_b):
    result = abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])
    return result


def nudge(point_a, point_b):
    nudge = 0
    if (
        ((point_a[0] + point_a[1]) % 2 == 0 and point_b[0] != point_a[0]) or
        ((point_a[0] + point_a[1]) % 2 == 1 and point_b[1] != point_a[1])
    ):
        nudge = 1

    return + (0.001 * nudge)
