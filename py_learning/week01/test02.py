from utils import log
from utils import ensure
from utils import isEquals
from utils import random_num, exchange


def test_01():
    arr = ['-', 1, 3, 3]
    for a in enumerate(arr):
        log('a', a)


# def insert_sort(arr, n):
#     if n == 0:
#         return
#     insert_sort(arr, n - 1)
#     i = n
#     while i > 0 and arr[i] < arr[i- 1]:
#         arr[i], arr[i - 1] = arr[i - 1], arr[i]
#         i -= 1
#         log('i', i, arr)
#     return arr


def test_02():
    arr = [random_num(1, 100) for i in range(8)]
    log('arr', arr)
    n = len(arr)
    new_arr = insert_sort(arr, n)
    log('new_arr', new_arr)




def insertsort(list):
    length = len(list)
    for current in range(1, length):
        for prev in range(current, 0, -1):
            if list[prev] < list[prev - 1]:
                exchange(list, prev, prev - 1)


def main():
    test_01()
    # test_02()


if __name__ == '__main__':
    main()
