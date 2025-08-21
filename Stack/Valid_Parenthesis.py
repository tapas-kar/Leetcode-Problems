# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Approach 1 - My Approach using a list as a stack
# Runtime: O(n)
# Space = O(n)

def isValid(s: str) -> bool:
    bracket_map = {'}': '{', ')': '(', ']':'['}

    cur_stack = []

    for i in s:
        if i not in bracket_map.keys():
            cur_stack.append(i)
        else:
            if cur_stack:
                if cur_stack[-1] == bracket_map[i]:
                    cur_stack.pop()
                else:
                    return False
            else:
                cur_stack.append(i)


    return len(cur_stack) == 0


# Approach 2 - Neetcode way
# He made a check where he is checking whether the current character from s is a closing parenthesis. 
# When you check for elements in a dictionary, you are essentially checking for the dictionary keys --> if c in bracket_map (that means if c in bracket_map.keys())
# He checked that the stack was not empty when it is a closing paranthesis because ")", "]", or "}" are not valid strings. You cannot add closing paranthesis to an empty stack
# So pop only if the stack is not empty and the last character matches the value of the mapping key by element c Else Return False

def isValid(s: str) -> bool:
    stack = []
    bracket_map = {'}': '{', ')': '(', ']':'['}

    for c in s:
        if c in bracket_map:
            if stack and stack[-1] == bracket_map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if len(stack) == 0 else False

