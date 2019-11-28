from const import OPERATORS
from datetime import datetime


def is_digit(string):
    if string.isdigit():
        return True
    try:
        float(string)
        return True
    except ValueError:
        return False


def str_to_date(date_text):
    try:
        return datetime.strptime(date_text, "%d-%m-%Y")
    except ValueError:
        return None


def calc_input():
    expression = []
    elements_count = input("Enter elements count(min 2) for arithmetic calculation or 1 for date: ")
    while not elements_count.isdigit() or int(elements_count) < 1:
        elements_count = input("Incorrect input. Try again: ")
    elements_count = int(elements_count)

    # date
    if elements_count == 1:
        for element_number in range(2):
            if element_number == 1:
                print('Only "-" operation allowed')
                expression += ['-']
            current_operand = input(f"Enter operand {element_number + 1}. Pattern - dd-mm-yyyy: ")
            current_operand = str_to_date(current_operand)
            while not current_operand:
                current_operand = input("Incorrect input. Try again: ")
                current_operand = str_to_date(current_operand)
            expression += [current_operand]
        return expression, 'date'

    # arithmetic
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
    return expression, 'arithmetic'
