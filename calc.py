from harder import calc
from newest import till, day


print('Datetime or numbers')
ch = input(str('choose Date or Num\nEnter "1" or "2": '))
try:

    if ch == '1':
        z = input('Past or future: ').lower()

        if z == 'past':
            day()

        elif z == 'future':
            till()

        else:
            print(':(')

    elif ch == '2':
        calc()

    else:
        print('Wrong input!')

except IndentationError or TypeError or ValueError or OverflowError:
    print('End of a line')