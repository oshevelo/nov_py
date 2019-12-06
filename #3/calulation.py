from math import e, pi
import datetime

def convert_to_date(date):
    pattern = '%d.%m.%Y'
    try:
        date = datetime.datetime.strptime(date.strip(), pattern).date()
        return date
    except Exception as e:
        print(e)

def calculate(user_input):
    try:
        date_list = user_input.split('-')
        if len(date_list) == 2:
            date1 = convert_to_date(date_list[0])
            date2 = convert_to_date(date_list[1])
            res = date1 - date2
            print(f'Result = {res}')
            return res
    except:
        print('Cannot evaluate statement as a date. Trying to evaluate with arithmetics...')

    try:
        res = eval(user_input, {'__builtins__': None}, {'e': e, 'pi': pi})
        print(f'Result = {res}')
        return res
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    except Exception as exception:
        print(f'Wrong statement is entered - {exception}')
