from simpleeval import simple_eval
from datetime import date, datetime


def is_digit(string):
    if string.isdigit():
        return True
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_date(string):
    try:
        datetime.strptime(string, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def is_operator(string):
    if string in ['+', '-', '*', '/', '//', '%', '**']:
        return True
    else:
        return False


def repeated_request(message, func_1, func_2):
    count = 3
    while count > 0:
        input_operand = input(f'Incorrect {message}. Try again:   ')
        if func_1(input_operand) or func_2(input_operand):
            return input_operand
        else:
            input_operand = ''
            count -= 1
            print(f'You have {count} attempts left')
    return input_operand


def to_calculate_digits(arg_1, arg_2, operand):
    try:
        result = simple_eval(arg_1 + operand + arg_2)
        print(f'result: {arg_1} {operand} {arg_2} = {result}')
    except Exception as e:
        print(e)


def to_calculate_dates(date_1, date_2):
    date_1_list = date_1.split('/')
    new_date_1 = date(int(date_1_list[2]), int(date_1_list[1]), int(date_1_list[0]))
    date_2_list = date_2.split('/')
    new_date_2 = date(int(date_2_list[2]), int(date_2_list[1]), int(date_2_list[0]))
    result = (new_date_1 - new_date_2).days
    print(f'result: {date_1} - {date_2} = {result} days')