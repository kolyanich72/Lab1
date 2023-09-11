class Stack:
    def __init__(self):
        self.stk = []
        self._len = 0
        self.res = True

    def push(self):
        self.stk.append(1)
        self._len += 1
        self.res = False
        return self.res

    def pop_(self):
        if self._len == 0:
            self.res = False
        else:
            self.stk.pop()
            self._len -= 1
            self.res = True
        return self.res


def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок
    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    q = Stack()

    for i in range(len(brackets_row)):
        if brackets_row[i] == "(":
            res = q.push()
        if brackets_row[i] == ")":
            res = q.pop_()
    return res
    # TODO реализовать проверку скобочной группы


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
#    print(check_brackets("()())("))  # False