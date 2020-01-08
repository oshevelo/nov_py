from dateutil.parser import *
from dateutil.relativedelta import *


def is_date(some_str):
    try:
        date = parse(some_str, dayfirst=True)
    except:
        return False
    else:
        return date
        # print(type(parse(some_str, dayfirst=True)))


def is_number(some_str):
    try:
        float(some_str)
    except:
        return False
    else:
        return True



def date_delta(s1, s2):
    s1 = is_date(s1)
    s2 = is_date(s2)
    print(s1, s2)

    return s1+relativedelta(s2)


def main():
    pass


if __name__ == '__main__':
    main()