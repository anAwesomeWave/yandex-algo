'''
Partition For QuickSort
https://www.youtube.com/watch?v=e3WhTm1G--o&t=1049s

e, g, n

'''
from random import randint


def partition(arr: list[int], left_ind: int, right_ind: int) -> list[int]:
    """ change array and return e, g pointers   [left, right) """
    pivot = arr[randint(left_ind, right_ind - 1)]
    eq_ind = left_ind
    gr_ind = left_ind
    for now_ind in range(left_ind, right_ind):
        if arr[now_ind] == pivot:
            arr[now_ind], arr[gr_ind] = arr[gr_ind], arr[now_ind]
            gr_ind += 1
        elif arr[now_ind] < pivot:
            tmp = arr[now_ind]
            arr[now_ind] = arr[gr_ind]
            arr[gr_ind] = arr[eq_ind]
            arr[eq_ind] = tmp
            eq_ind += 1
            gr_ind += 1
    return [eq_ind, gr_ind]


def quicksort(arr: list[int], left_ind: int, right_ind: int):
    """
        [left_ind, right_ind)
        1. partition -> split in three parts
        2. sort < pivot and > pivot parts
        3.combine and return the answer
    """
    if left_ind == right_ind:
        return
    eq, gr = partition(arr, left_ind, right_ind)
    quicksort(arr, left_ind, eq)
    quicksort(arr, gr, right_ind)


arr = [1, 1, 1]
# print(partition(arr, 0, len(arr)))
# print(arr)

print('------')
quicksort(arr, 0, len(arr))
print(arr)