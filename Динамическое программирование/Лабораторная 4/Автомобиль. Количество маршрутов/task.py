from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
     # TODO решить задачу с помощью динамического программирования
   

    return table

if __name__ == '__main__':
    paths = car_paths(5, 5)
 #   paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
    print(paths)

