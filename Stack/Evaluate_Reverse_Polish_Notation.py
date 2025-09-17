# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# Approach 1 - My approach - I did use a stack and I did pop 2 operands whenever I encountered an operator in the list > performed the operation > pushed the result back on top of the stack
# Fixed the edge case where a negative division was not getting truncated to 0 by Defining my division function in terms of number line where 
# if a division result is between -1 and 0, I use math.ceil to round up to 0
# else if a division result is between 0 and 1, I use math.floor to round down to 0
# else, otherwise a division result will be an integer division ex: x//y

import math

def evalRPN(tokens: list[str]) -> int:

    num_stack = []

    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        if x/y < 0 and x/y > -1:
            return math.ceil(x/y)
        elif x/y > 0 and x/y < 1:
            return math.floor(x/y)
        else:
            return x//y

    operators = ["+", "-", "*", "/"]

    for i in range(len(tokens)):
        if tokens[i] not in operators:
            num_stack.append(tokens[i])
        else:
            if num_stack:
                op2 = int(num_stack.pop())
                op1 = int(num_stack.pop())
            if tokens[i] == "+":
                result = add(op1, op2)
            if tokens[i] == "-":
                result = subtract(op1, op2)
            if tokens[i] == "*":
                result = multiply(op1, op2)
            if tokens[i] == "/":
                result = divide(op1, op2)
            
            num_stack.append(result)

    return num_stack[-1] if num_stack else -1
            