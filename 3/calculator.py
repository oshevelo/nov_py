import operator
from datetime import datetime
from type_check import is_number, is_date


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}


def main():
    print('\nits very simple calculator')
    print('supported number`s operators: +, -, *, /, **')
    print('and date`s offset: +, - ')
    print('PS enter 0 as operator to exit')

    while True:
        first_operand = input('\ninput a: ')
        second_operand = input('input b: ')

        if is_number(first_operand) and is_number(second_operand):
            a = float(first_operand)
            b = float(second_operand)
            print('you entered a numbers {} and {}'.format(a, b))
            operator = input('input operator: ')
            print(number_calculate(a, b, operator))
        elif is_date(first_operand):
            a = is_date(first_operand)
            print('you entered a date', a)
        else:
            print('unclear operand... try again...')


def number_calculate(a, b, operator):
    if operator == '+':
        print('result =', a+b)
    elif operator == '-':
        print('result =', a-b)
    elif operator == '*':
        print('result =', a*b)
    elif operator == '/':
        print('result =', a/b) if b else print('Error: zero division')
    elif operator == '**':
        print('result =', pow(a, b))


def date_calculate(a, b, operand):
    pass


if __name__ == '__main__':
    main()
