
#TODO implement standart constants
#TODO add zero division catcher

import operator
import sys

#add spaces between tokens from user input for .list method to work properly
def addspace(string):
    result = ''
    for char in string:
        result = result + char + ' '
    return result

#Implement Shunting yard algorithm

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


#define operation precedence (additive under multiplicative under exponentiation)

def higher_precedence(op1, op2):
    pre = {'+':0, '-': 0, '*':1, '/':1, '^':2}
    return pre[op1] >= pre[ op2]

#define associativity of the operator 0 - for left and 1 - for right

def associativity(op):
    assoc = {'+':0, '-':0, '*':0, '/':0, '^':1}
    return assoc[op]


def build_tree(exp):
    exp_list = exp.split()
    #print(exp_list)
    stack = []
    tree_stack = []
    for i in exp_list:
        #case for operands
        if i not in ['+', '-', '*', '/', '^', '(', ')']:
            #convert string to number
            t = Node(float(i))
            #add to the calculation stack
            tree_stack.append(t)
        #case for operators
        elif i in ['+', '-', '*', '/', '^']:
                #check that operator stack is not empty and does not contain opening brackets
                if not stack or stack[-1] == '(':
                    stack.append(i)
                #if empty or brackets are opened, check the precedence of current operator
                #case when current operator has higher precendence than existing in the stack
                elif higher_precedence(i, stack[-1]) and associativity(i) == 1:
                    stack.append(i)

                #case when current operator has lower precedence than existing in the stack
                #pop it from stack and construct a tree
                else:
                    while stack and higher_precedence(stack[-1], i) and associativity(i) == 0:
                        popped_item = stack.pop()
                        t = Node(popped_item)
                        t1 = tree_stack.pop()
                        t2 = tree_stack.pop()
                        t.right = t1
                        t.left = t2
                        tree_stack.append(t)
                    stack.append(i)
        #case for opening brackets
        elif i == '(':
            stack.append('(')
        #case for closing brackets
        elif i == ')':
            while stack[-1] != '(':
                popped_item = stack.pop()
                t = Node(popped_item)
                t1 = tree_stack.pop()
                t2 = tree_stack.pop()
                t.right = t1
                t.left = t2
                tree_stack.append(t)
            stack.pop()
    #construct tree from stack
    while stack:
        popped_item = stack.pop()
        t = Node(popped_item)
        t1 = tree_stack.pop()
        t2 = tree_stack.pop()
        t.right = t1
        t.left = t2
        tree_stack.append(t)

    t = tree_stack.pop()

    return t


#evaluation of constructed tree
def evaluate(expTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '^':operator.pow}

    leftC = expTree.left
    rightC = expTree.right
    #recursively call evaluation function to traverse the tree
    if leftC and rightC:
        fn = opers[expTree.data]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return expTree.data


# define function to check that all brackets in expression entered by user are balanced
def brackets_check(inp_string):
    stack = []
    for i in inp_string:                                            # loop over input
        if i == "(":                                                # if opening bracket found
            stack.append(i)                                         # add opening brackets to stack
        elif i == ")":                                              # if closing bracket found
            if len(stack) > 0 and stack[len(stack) - 1] == "(":     # check if opening bracket is already there
                stack.pop()                                         # if yes delete it (i.e. close brackets pair and empty stack)
            else:
                sys.exit("Invalid expression. Wrong use of brackets. Exiting...") # if first bracket found is closing, raise error and exit the program
        if len(stack) == 0:                                         # if stack is empty after all iterations
            pass                                                    # do nothing
        else:
            sys.exit("Invalid expression. Wrong use of brackets. Exiting...")


# main executable

if __name__ == '__main__':

    # getting user's input
    user_input = input("Please enter your expression to be calculated")

    # check that expression entered by user has balanced brackets
    brackets_check(user_input)

    #add spaces for split method to work properly
    user_input = addspace(user_input)

    #build an AST from user's input
    t=build_tree(str(user_input))

    #print the result of AST evaluation
    print("=", format(evaluate(t)))


else:
    pass