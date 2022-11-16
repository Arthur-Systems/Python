# author: Arthur Wei
# date: November 14, 2022
# file: calculator.py a python file that calulates the value of an infix expression and converts it to postfix
# input: An infix expression to be calculated
# output: The value of the expression and the postfix expression

import stack as Stack
import tree as BT


def infix_to_postfix(infix: str) -> str:
    operator = ['+', '-', '*', '/', '(', ')', '^']
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    opstack = Stack.Stack()
    output = ''
    for ind, symb in enumerate(infix):
        # checks the symbol is a number and the next symbol is not an operator or a space
        if symb not in operator and infix[ind + 1] not in operator and infix[ind + 1] != ' ' if ind < len(infix) - 1 else False:
            output += symb  # adds the number to the output without a space
        elif symb not in operator and infix[ind + 1] in operator if ind < len(infix) - 1 else True:
            output += symb + ' '
        elif symb == '(':
            opstack.push(symb)
        elif symb == ')':
            while opstack.size() > 0 and opstack.peek() != '(':
                output += opstack.pop() + ' '
            opstack.pop()
        else:
            # if the precedence of the operator on the stack is greater than or equal to the precedence of the current operator
            while opstack.size() > 0 and opstack.peek() != '(' and precedence[opstack.peek()] >= precedence[symb]:
                # pop the operator from the stack and add it to the output
                output += opstack.pop() + ' '
            opstack.push(symb)  # push the current operator onto the stack
    while opstack.size() > 0:
        output += opstack.pop() + ' '
    if output[-1] == ' ':
        output = output[:-1]
    output = output.replace(')', ' ')
    output = output.replace('(', ' ')
    return output


def calculate(infix: str) -> float:
    postfix = infix_to_postfix(infix)
    tree = BT.ExpTree.make_tree(postfix.split())
    return BT.ExpTree.evaluate(tree)


# a driver to test calculate module
if __name__ == '__main__':
    print("Welcome to Calculator Program!")
    while True:
        infix = str(input(
            "Please enter your expression here. To quit enter 'quit' or 'q':\n"))
        if infix == 'quit' or infix == 'q':
            break
        else:
            print(calculate(infix))
    print("Goodbye!")
