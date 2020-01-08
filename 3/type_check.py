from dateutil.parser import *
from dateutil.relativedelta import *

from datetime import datetime


def is_date(some_str):
    try:
        parse(some_str, dayfirst=True)
    except Exception as e:
        print(e)
    else:
        print(type(parse(some_str, dayfirst=True)))
        print(isinstance(parse(some_str, dayfirst=True), datetime))
        return parse(some_str, dayfirst=True)

def is_number(some_str):
    try:
        float(some_str)
    except:
        return False
    else: return True



def date_delta(s1, s2):
    s1 = is_date(s1)
    s2 = is_date(s2)
    print(s1, s2)

    return s1+relativedelta(s2)


def main():
    pass


if __name__ == '__main__':
    main()