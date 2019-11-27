import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}
# priority = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
priority = ['**', '*', '/', '+', '-']

sequence = []

count = input('element count (>=2): ')

sequence.append(input('input number: '))
for i in range(1, int(count)):
    sequence.append(input('input operation: '))
    sequence.append(input('input number: '))

print(sequence)


def make_operation(number_left, number_right, operation):
    return operations[operation](number_left, number_right)
