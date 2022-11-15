#
# DO NOT FORGET TO ADD COMMENTS!!!
#

import stack as Stack
import tree as BT


def infix_to_postfix(infix: str) -> str:
    operator = ['+', '-', '*', '/', '(', ')', '^']
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack.Stack()
    output = ''
    for char in infix:
        if char not in operator:
            output += char
        elif char == '(':
            stack.push('(')
        elif char == ')':
            while stack.size() > 0 and stack.peek() != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack.size() > 0 and stack.peek() != '(' and precedence[stack.peek()] >= precedence[char]:
                output += stack.pop()
            stack.push(char)
    while stack.size() > 0:
        output += stack.pop()
    return output


def calculate(infix: str) -> float:
    pass


# a driver to test calculate module
if __name__ == '__main__':
    print("Welcome to Calculator Program!")
    # infix = input(
    #     "Please enter your expression here. To quit enter 'quit' or 'q':")
    # if infix == 'quit' or infix == 'q':
    #     print("Goodbye!")
    # else:
    print(infix_to_postfix('4+2-5*3+(2^3)*7/3/1*2+2^4^3+8'))

    # # test infix_to_postfix function
    # assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    # assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # # test calculate function
    # assert calculate('(5+2)*3') == 21.0
    # assert calculate('5+2*3') == 11.0
