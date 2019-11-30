import calculation

def repeat(func, message):
    answer = ''
    while answer.upper() != 'N':
        answer = input('Do you want to repeat? Enter Y/N:')
        if answer.upper() == 'Y':
            user_input = input(message)
            func(user_input)
        elif answer.upper() != 'N':
            print('Wrong answer! You should enter Y or N')
            continue

message = 'Enter a statement to calculate:'
user_input = input(message)
calculation.calculate(user_input)
repeat(calculation.calculate, message)

