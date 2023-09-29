from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами
    1. Определите максимальное значение в массиве и заполните
        вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    max_elem = max(container)
    di = {i:0 for i in range(0, max_elem+1)}

    while 0 < len(container):
        elem = container.pop()
        di[elem] += 1

    for key, value in di.items():
        for i in range(value):
            container.append(key)

    return container


if __name__ == "__main__":
    a = [4, 3, 1, 4, 5, 2, 4, 1, 7, 3, 1, 10, 2, 0, 1]
    print(sort(a))

