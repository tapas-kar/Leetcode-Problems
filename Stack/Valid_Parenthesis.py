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
def isValid(s: str) -> bool:

    rs = []
    
    if len(s) == 0:
        return True
    
    if len(s) == 1:
        return False
    
    rs.append(s[0])

    for i in s[1:]:

        
        if i in ["(", "{", "["]:
            rs.append(i)
        
        if i == ")" and rs[-1] == "(":
            rs.pop()
        if i == "}" and rs[-1] == "{":
            rs.pop()
        if i == "]" and rs[-1] == "[":
            rs.pop()
    
    return len(rs) == 0




# Approach 2: Hint: Use a hashmap to keep track of the close to open parenthesis
# Try it yourself...

s = "()"

print(isValid(s))