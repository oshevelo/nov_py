from calc_functions import is_digit, is_date, is_operator, repeated_request, to_calculate_digits, to_calculate_dates

while True:
    operand_1 = input('Enter the first operand DIGIT or DATE(as d/m/y --> 01/11/2019):   ')
    if not is_digit(operand_1) and not is_date(operand_1):
        operand_1 = repeated_request(
            message='the first operand DIGIT or DATE(as d/m/y --> 01/11/2019)', func_1=is_digit, func_2=is_date)
    if operand_1 == '':
        break

    operand_2 = input('Enter the second operand DIGIT or DATE(as d/m/y --> 01/11/2019):   ')
    if not is_digit(operand_2) and not is_date(operand_2):
        operand_2 = repeated_request(
            message='the second operand DIGIT or DATE(as d/m/y --> 01/11/2019)', func_1=is_digit, func_2=is_date)
    if operand_2 == '':
        break

    my_operator = input('Enter the operator:   ')
    if not is_operator(my_operator):
        my_operator = repeated_request(message='operator', func_1=is_operator, func_2=is_operator)
    if my_operator == '':
        break

    if is_digit(operand_1) and is_digit(operand_2):
        to_calculate_digits(operand_1, operand_2, my_operator)
    elif is_date(operand_1) and is_date(operand_2):
        if my_operator == '-':
            to_calculate_dates(operand_1, operand_2)
        else:
            print('Incorrect operator for dates')
    else:
        print('Operators are not the same type')

    new_answer = input('One more time?  (Y/N):   ')
    if new_answer.upper() != 'Y':
        break
