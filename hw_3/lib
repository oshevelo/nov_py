from datetime import datetime
import string


def foo_input_float(msg):
    i = 5
    while i != 0:
        try:
            return float(input(f'введите {msg}'))
        except ValueError:
            i -= 1
            print(f'{msg}это не число, введите, число. у вас осталось {i} попыток')


operations = {'+': lambda a, b: a+b,
              '-': lambda a, b: a-b,
              '*': lambda a, b: a*b,
              '/': lambda a, b: a/b if b != 0 else print('извините, деление на ноль не возможно'),
              '**': lambda a, b: a**b
              }


def foo_input_oper():
    i = 5
    while i != 0:
        oper = input('введите желаемую операцию - + / * или **')  # проверяем что бы ввели мат.операцию, с кол-вом попыток продолжаем
        if oper not in operations:
            i -= 1
            print(f'извините вы ввели не математическую операцию, повторите ввод. у вас осталось {i} попыток')  # проверяем что бы ввели мат.операцию, с кол-вом попыток продолжаем
        else:
            return oper


def foo_date_input(msg):
    i = 5
    while i != 0:
        date_us = input(f'введите {msg} дату в формате: дд.мм.гггг')
        for s in date_us:
            if s in string.punctuation:
                date_us = date_us.replace(s,'.')
        try:
            date_us = datetime.strptime(date_us, '%d.%m.%Y').date()
            return date_us
        except:
            try:
                date_us = datetime.strptime(date_us, '%d.%m.%y').date()
                return date_us
            except ValueError:
                i -= 1
                print(f'вы ввели не дату, попробуйте снова, осталось {i} попытки')


def ask_day_or_calc():
    while True:
        try:
            ask = int(input('какую операцию желаете произвести: 1. калькулятор или 2. вычисление дат? выеберете 1 или 2'))
        except ValueError:
            print('это не число пробуйте снова')
        else:
            if ask != 1 and ask != 2:
                print('вариантов всего два, sorry')
            else:
                return ask


def check_date_str(user_srt):
    for s in user_srt:
        if s in string.punctuation:
            user_srt = user_srt.replace(s, '.')
    try:
        date_us = datetime.strptime(user_srt, '%d.%m.%Y').date()
        return date_us
    except:
        try:
            date_us = datetime.strptime(user_srt, '%d.%m.%y').date()
            return date_us
        except:
            pass
