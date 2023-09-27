def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        raise ValueError
    l_ = iter(range(n+1))
    res = 1
    for i in range(n+1):
        n1 = next(l_)

        if n1 != 0:
            res *= n1

    return res


if __name__ == "__main__":
    n2 = 5
    print(factorial_iterative(n2))
