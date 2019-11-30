from math import e, pi
import datetime

def convert_to_date(date):
    patterns = ['%Y%m%d', '%Y-%m-%d', '%Y.%m.%d', '%Y:%m:%d', '%Y/%m/%d', '%Y\%m\%d',
                '%d%m%Y', '%d-%m-%Y', '%d.%m.%Y', '%d:%m:%Y', '%d/%m/%Y', '%d\%m\%Y']
    for i in patterns:
        try:
            date = datetime.datetime.strptime(date.strip(), i).date()
            return date
        except:
            pass

def calculate(user_input):
    try:
        date_list = user_input.split('-')
        if len(date_list) == 2:
            date1 = convert_to_date(date_list[0])
            date2 = convert_to_date(date_list[1])
        elif len(date_list) == 6: # для 2019-10-10-2018-12-12
            date1 = convert_to_date(date_list[0] + '.' + date_list[1] + '.' + date_list[2])
            date2 = convert_to_date(date_list[3] + '.' + date_list[4] + '.' + date_list[5])
        res = date1 - date2
        print(f'Result = {res}')
        return res
    except:
        pass

    try:
        res = eval(user_input, {'__builtins__': None}, {'e': e, 'pi': pi})
        print(f'Result = {res}')
        return res
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    except Exception as exception:
        print(f'Wrong statement is entered - {exception}')