"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве
    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """

    if len(arr) == 0:
        raise ValueError

    min_ = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < arr[min_]:
            min_ = i

    return min_


if __name__ == "__main__":
    print(min_search([5, 3, 15, 20, 2, 25, 22, 2, 10, 2, 8]))