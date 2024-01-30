def find_symm(points: list) -> bool:
    """
    list - unhashable, чтобы он был ключом словаря превратим еего в строку
    """
    prob_symm = min(p[0] for p in points) + (max(p[0] for p in points) - min(p[0] for p in points)) / 2

    d_of_seen = {}
    for point in points:
        point_str = f"{float(point[0])} {point[1]}"
        if point_str not in d_of_seen:
            d_of_seen[point_str] = 0
        d_of_seen[point_str] += 1
    print(d_of_seen)
    for point in points:
        dist = prob_symm - point[0]
        symm_point = f"{prob_symm + dist} {point[1]}"
        if symm_point in d_of_seen:
            d_of_seen[symm_point] -= 1
            if d_of_seen[symm_point] == 0:
                del d_of_seen[symm_point]
        else:
            return False
    return True


assert find_symm([[0, 0], [1, 4], [3, 3], [5, 4], [6, 0]]) is True

assert find_symm([[0, 0], [6, 0]]) is True

assert find_symm([[0, 5], [6, -5]]) is False

assert find_symm([[3, 1], [0, 0], [-3, 1]]) is True
