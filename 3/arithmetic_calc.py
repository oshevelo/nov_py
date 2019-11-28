from const import OPERATORS


def calc(expression):
    try:
        first_priority_count = expression.count('*') + expression.count('/')
        for i in range(first_priority_count):
            for j in range(len(expression)):
                if expression[j] == '*' or expression[j] == '/':
                    left = float(expression[j-1])
                    operator = expression.pop(j)
                    right = float(expression.pop(j))
                    expression[j - 1] = OPERATORS[operator](left, right)
                    break

        # calculation + -
        first_priority_count = expression.count('+') + expression.count('-')
        for i in range(first_priority_count):
            for j in range(len(expression)):
                if expression[j] == '+' or expression[j] == '-':
                    left = float(expression[j-1])
                    operator = expression.pop(j)
                    right = float(expression.pop(j))
                    expression[j - 1] = OPERATORS[operator](left, right)
                    break
        return expression[0]
    except ZeroDivisionError:
        print('Error. Division by zero')
        return None
