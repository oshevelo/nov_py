# 2.3 var
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

# 2.2 var
# from math import *
# 
# def repeat(func, message):
#     answer = ''
#     while answer.upper() != 'N':
#         answer = input('Do you want to repeat? Enter Y/N:')
#         if answer.upper() == 'Y':
#             user_input = input(message)
#             func(user_input)
#         elif answer.upper() != 'N':
#             print('Wrong answer! You should enter Y or N')
#             continue
# 
# def calculate(user_input):
#     try:
#         amount_of_nums = int(user_input)
#         i = 2
#         result = input('Enter 1 num:')
#         try:
#             result = float(result)
#         except Exception as e:
#             print('Wrong statement is entered - this should be an integer or float value.')
#             return None
#         while i < amount_of_nums + 1:
#             op = input('Enter an operation (+,-,*,/)').strip()
#             tmp2 = input(f'Enter {i} num:')
#             try:
#                 tmp2 = float(tmp2)
#                 if op == '+':
#                     result += tmp2
#                 elif op == '-':
#                     result -= tmp2
#                 elif op == '*':
#                     result *= tmp2
#                 elif op == '/':
#                     try:
#                         result /= tmp2
#                     except ZeroDivisionError as e:
#                         print('Cannot divide by zero.')
#                         return None
#                 else:
#                     print('Wrong operation.')
#                     return None
#             except Exception as exception:
#                 print('Wrong statement is entered - this should be an integer or float value.')
#                 return None
#             i += 1
#         print(f'Result = {result}')
#         return result
#     except Exception as exception:
#         print('Wrong statement is entered - this should be an integer.')
#         return None
# 
# message = 'Enter an amount of nums to calculate:'
# user_input = input(message)
# calculate(user_input)
# repeat(calculate, message)
