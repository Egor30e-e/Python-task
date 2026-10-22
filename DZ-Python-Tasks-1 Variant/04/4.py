import math


def distance(points, x0, y0):  # points - это массив точек
    if len(points) == 0:
        return None

    best = points[0]  # (1, 2)
    x, y = best
    best_sq = (x - x0) ** 2 + (y - y0) ** 2
    for x, y in points[1:]:
        dist_sq = (x - x0) ** 2 + (y - y0) ** 2
        if dist_sq < best_sq:  # знак ставится в зависимости от условия (тут про равно)
            best_sq = dist_sq
            best = (x, y)
    distance = math.sqrt(best_sq)

    return best, distance


points = [(1, 2), (5, 2), (10, 9)]

print(distance(points, 3, 3))
