from input import calc_input
from arithmetic_calc import calc as arithmetic_calc
from date_calc import calc as date_calc


try:
    expression, type = calc_input()
    if type == 'arithmetic':
        print("Input: ", ' '.join(expression))
        result = arithmetic_calc(expression)
        if result is not None:
            print(f'Result: {result}')
    elif type == 'date':
        print("Input: {0} {1} {2}".format(
            expression[0].strftime("%d-%m-%Y"), expression[1], expression[2].strftime("%d-%m-%Y")))
        result = str(date_calc(expression))
        print(f'Result: {result}')
    else:
        raise Exception('Error. Unknown calculation type')
except Exception as e:
    print(e)
