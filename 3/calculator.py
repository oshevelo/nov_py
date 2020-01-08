from some_file import is_number, is_date


def main():
    print('\nits very simple calculator')
    print('supported number`s operators: +, -, *, /, **')
    print('and date`s ')
    print('PS enter 0 as operator to exit')

    while True:
        f_operand = input('\ninput a: ')

        if is_number(f_operand):
            print('you entered a number', float(f_operand))
        elif is_date(f_operand):
            print('you entered a date', is_date(f_operand))
        else:
            print('unclear operand... try again...')


def compute
        # try:
        #     f_operand = float(input('\ninput a: '))
        # except ValueError:
        #     print('a not numbers...')
        #     print(is_date(a))
        # else:
        #     operator = input('operator: ')
        #
        #     if operator == '+':
        #         print('result =', a+b)
        #     elif operator == '-':
        #         print('result =', a-b)
        #     elif operator == '*':
        #         print('result =', a*b)
        #     elif operator == '/':
        #         print('result =', a/b) if b else print('Error: zerro division')
        #     elif operator == '**':
        #         print('result =', pow(a, b))
        #     elif operator == '0':
        #         print('thanks for using the calculator')
        #         break
        #     else:
        #         print('operator is not supported')

if __name__ == '__main__':
    main()
