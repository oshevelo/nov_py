# define math operations

def operation(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        # zero division handling
        try:
            num1 / num2
        except ZeroDivisionError:
            print("Division by zero. Exiting...")


# define function to check that all brackets in expression entered by user are balanced

def brackets_check(inp_string):
    stack = []
    for i in inp_string:                                            # loop over input
        if i == "(":                                                # if opening bracket found
            stack.append(i)                                         # add opening brackets to stack
        elif i == ")":                                              # if closing bracket found
            if len(stack) > 0 and stack[len(stack) - 1] == "(":     # check if opening bracket is already there
                stack.pop()                                         # if yes delete it (i.e. close brackets pair)
            else:
                raise Exception(
                    "Invalid expression. Wrong use of brackets")    # if first bracket found is closing, raise error and exit the program
        if len(stack) == 0:                                         # if stack is empty after all iterations
            pass                                                    # do nothing


# main executable
if __name__ == '__main__':
    # getting user's input

    user_input = input("Please enter your expression to be calculated")

    # check that expression entered by user has balanced brackets
    brackets_check(user_input)

    # parse user input into a list
    parsedInput = list(user_input)

    
else:
    pass
