"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self.que = []
        # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди
        :param elem: Элемент, который должен быть добавлен
        """
        self.que.append(elem)
        # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if len(self.que) == 0:
            raise IndexError("Ошибка, если очередь пуста")
        return self.que.pop()

        # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("указан не целочисленный тип индекса")
        if len(self.que) < ind:
            raise IndexError("если индекс вне границ очереди")
        return self.que[ind]
        # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self.que.clear()
         # TODO реализовать метод clear

    def __str__(self):
        return f"{self.que}"

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self.que)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    print(f" init que {q}")
    print(q.dequeue())
    print(f" sec que {q}, len-{len(q)}")
    print(q.peek(1))
    q.clear()
    print(f" thrd que {q}, len-{len(q)}")