from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком
    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    while True:
        flag = 0
        for i in range(1, len(container)):

            if container[i] < container[i-1]:
                container[i-1], container[i] = container[i], container[i-1]
                flag += 1

        if flag == 0:
            return container


if __name__ == "__main__":
    print(sort([3, 5, 4, 7, 1, 10, 2, 0]))
