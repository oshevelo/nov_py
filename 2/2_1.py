OPERATORS = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: x / y}


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def calc_input():
    expression = []
    operand_1 = input(f"Enter operand 1: ")
    while not is_digit(operand_1):
        operand_1 = input("Incorrect input. Try again: ")
    expression += [operand_1]

    operator = input(f"Enter operator ( + - * / ): ")
    while operator not in OPERATORS:
        operator = input("Incorrect input. Try again: ")
    expression += [operator]

    operand_2 = input(f"Enter operand 2: ")
    while not is_digit(operand_2):
        operand_2 = input("Incorrect input. Try again: ")
    expression += [operand_2]

    return expression


def calc_eval(expression):
    try:
        return OPERATORS[expression[1]](float(expression[0]), float(expression[2]))
    except ZeroDivisionError:
        print('Error. Division by zero')
        return None


expression = calc_input()
print("Input: ", ' '.join(expression))
result = calc_eval(expression)
if result is not None:
    print(f'Result: {result}')
