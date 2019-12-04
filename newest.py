import datetime


def day():

    try:

        t_day = datetime.date.today()
        delta = int(input('Enter a count of days: '))
        t_delta = datetime.timedelta(delta)
        zer = t_day - t_delta
        print(zer.strftime('%B %d, %Y'))

    except TypeError or OverflowError or ValueError:
        print('Invalid input')


def till():

    try:

        t_day = datetime.date.today()
        y = int(input('Enter a year: '))
        m = int(input('Enter a month: '))
        d = int(input('Enter a day: '))
        td = datetime.date(y, m, d)
        zer = td - t_day
        print(f'{zer.days} left')

    except IndentationError or TypeError or ValueError or OverflowError:
        print('Invalid input')