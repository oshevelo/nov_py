from math import *

def repeat(func, message):
    answer = ''
    while answer.upper() != 'N':
        answer = input('Do you want to repeat? Enter Y/N:')
        if answer.upper() == 'Y':
            user_input = input(message)
            func(user_input)
        elif answer.upper() != 'N':
            print('Wrong answer! You should enter Y or N')
            continue

def calculate(user_input):
    try:
        res = eval(user_input, {'__builtins__': None}, {'e': e, 'pi': pi})
        print(f'Result = {res}')
        return res # на будущее
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    except Exception as exception:
        print(f'Wrong statement is entered - {exception}')

message = 'Enter a statement to calculate:'
user_input = input(message)
calculate(user_input)
repeat(calculate, message)