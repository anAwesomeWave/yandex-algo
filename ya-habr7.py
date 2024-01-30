"""
Слияние отрезков:

Вход: [1, 3] [100, 200] [2, 4]
Выход: [1, 4] [100, 200]

O(n * log n)
сортируем по первой коорд. двигаемся направо
пока старт меньше тек максимума, собираем отрезки в 1


[1, 3], [2, 2], [3, 5] -> [1, 5]
"""


def sol1(segments: list[list[int]]) -> list[list[int]]:
    segments.sort(key=lambda seg: seg[0])
    ans = []
    if len(segments) == 0:
        return segments
    started_num = segments[0][0]
    cur_max = segments[0][1]
    for seg in segments:
        if seg[0] <= cur_max:
            cur_max = max(cur_max, seg[1])
        else:
            ans.append([started_num, cur_max])
            started_num = seg[0]
            cur_max = seg[1]
    ans.append([started_num, cur_max])
    return ans


arr1 = [[1, 3], [100, 200], [2, 4]]
ans1 = [[1, 4], [100, 200]]

arr2 = [[3, 5], [2, 2], [1, 3]]
ans2 = [[1, 5]]

arr3 = [[1, 2]]
ans3 = [[1, 2]]

arr4 = [[3, 5], [1, 2]]
ans4 = [[1, 2], [3, 5]]

arr5 = []
ans5 = []

assert sol1(arr1) == ans1
assert sol1(arr2) == ans2
assert sol1(arr3) == ans3
assert sol1(arr4) == ans4
assert sol1(arr5) == ans5
