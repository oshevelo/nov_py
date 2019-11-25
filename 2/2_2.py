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
    elements_count = input("Enter elements count(min 2): ")
    while not elements_count.isdigit():
        elements_count = input("Incorrect input. Try again: ")
    elements_count = int(elements_count)

    for element_number in range(elements_count):
        if element_number > 0:
            current_operator = input(f"Enter operator {element_number} ( + - * / ): ")
            while current_operator not in OPERATORS:
                current_operator = input("Incorrect input. Try again: ")
            expression += [current_operator]

        current_operand = input(f"Enter operand {element_number + 1}: ")
        while not is_digit(current_operand):
            current_operand = input("Incorrect input. Try again: ")
        expression += [current_operand]
    return expression


def calc_eval(expression):
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


expression = calc_input()
print("Input: ", ' '.join(expression))
result = calc_eval(expression)
if result is not None:
    print(f'Result: {result}')
