import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}

# operators_list = ['+', '-', '*', '/', '**']
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

numbers_stack = []
operations_stack = []

count = input('enter element count: ')

operations_stack.append(input())

for i in range(2, int(count)):
    print(operations_stack, operations_stack)

    operator = input()

    if operations and operations_stack[-1] > operator:
        pass

    operations_stack.append(input())
    operations_stack.append(input())

print('operator', count)


def operation(number_left, number_right, operator):
    return operations[operator](number_left, number_right)


if __name__ == '__main__':
    calculator()
