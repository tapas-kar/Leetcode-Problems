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
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.





# Approach 1: The dumb approach; of course it failed some test cases
# def isValid(s: str) -> bool:

#     rs = []
    
#     if len(s) == 0:
#         return True
    
#     if len(s) == 1:
#         return False
    
#     rs.append(s[0])

#     for i in s[1:]:

        
#         if i in ["(", "{", "["]:
#             rs.append(i)
        
#         if i == ")" and rs[-1] == "(":
#             rs.pop()
#         if i == "}" and rs[-1] == "{":
#             rs.pop()
#         if i == "]" and rs[-1] == "[":
#             rs.pop()
    
#     return len(rs) == 0




# Approach 2: Hint: Use a hashmap to keep track of the close to open parenthesis
# Try it yourself...

# Explanation in my own words:
# Make a stack to keep track of ALL the parenthesis
# Define a dictionary (AKA a hashmap) that will have the correct pairings for the opposite parenthesis; for ex: ) for (, ] for [, and } for {
# For every character in the input string:
    # if the character is in the hashmap described above (that means the current character is actually one of the 3 closing parenthesis) then:
        #      if the stack is NOT empty AND the character that we are encountering has a complementary open parenthesis then:
        #           pop from the stack --> At this point, it means that the current character is the respective closing parenthesis for the open one on top of the stack
        #      else:
        #           we can return False here because --> the current character that we encountered (which is a closing parenthesis) does NOT have a matching open parenthesis on top of the stack--> that means the input string is NOT a valid parenthesis
    # else (this means that the current character that we encountered is NOT a closing parenthesis BUT an open parenthesis):
        # append this character to the stack (that way only open parenthesis will be added on to the stack and will sit on top)
    
# After we are done traversing each character in the input string, we can safely return True if the stack is empty or False if it is NOT

def isValid(s: str) -> bool:

    stack = []

    close_to_open = {")" : "(", "}" : "{", "]" : "["}

    for i in s:
        if i in close_to_open:
            if stack and stack[-1] == close_to_open[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    
    return True if not stack else False


s = "])"

print(isValid(s))