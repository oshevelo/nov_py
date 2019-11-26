__author__ = 'ME'
# Implement calc
# 1)
# enter a 10
# enter b 20
# enter op +
# result=30


def is_digit(string):                                           # string ->  |f| -> digit or None
    if string.isdigit():
        return int(string)
    else:
        try:
            return float(string)
        except Exception as e:
            print('Looser! It is not digit')


def y_n_question(my_func, msg_1='', msg_2=''):                  # re-entry of incorrect data or None
    while True:
        answer = input(msg_1+' (Y/N)')
        if answer.upper() == 'Y':
            res = my_func(input(f'enter the {msg_2}:   '))
            if res:
                return res
        elif answer.upper() == 'N':
            break
        else:
            print('Don\'t understand')


def calculation(arg_1, arg_2, operator):                        # operation calculation
    try:
        result = eval(str(arg_1)+operator+str(arg_2))
        print(f'result: {a} {operator} {b} = {result}')
    except Exception as e:
        print(e)


while True:
    a = is_digit(input('enter the first digit:   '))
    if a is None:
        a = y_n_question(is_digit, 'repeat', 'digit')
    if a is None:
        break

    b = is_digit(input('enter the second digit:   '))
    if b is None:
        b = y_n_question(is_digit, 'repeat', 'digit')
    if b is None:
        break

    my_operator = input('enter the operator:   ')
    while my_operator not in ['+', '-', '*', '/', '//', '%', '**']:
        my_operator = None
        print('Looser! It is not operator')
        user_input_ask = input('repeat it (Y/N) ???: ')
        while user_input_ask.upper() not in ['Y', 'N']:
            user_input_ask = input('repeat it (Y/N) ???: ')
        if user_input_ask.upper() == 'N':
            break
        else:
            my_operator = input('enter the operator:   ')
    if  my_operator is None:
        break

    calculation(a, b, my_operator)

    new_ask = input('to count again?  (Y/N):   ')
    if new_ask.upper() != 'Y':
        break
