from const import OPERATORS


def calc(expression):
    left = expression[0]
    operator = expression[1]
    right = expression[2]
    return OPERATORS[operator](left, right)