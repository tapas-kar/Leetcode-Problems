# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# Approach 1 - Neetcode Approach (Recursive approach)
# Runtime: O((4 ** n)/sqrt(n))
# Space: O(n)

def generateParentheses(n: int) -> list[str]:
    # only add open parentheses if open_count < n
    # only add a closing parentheses if closed_count < open
    # Valid IIF open_count == closed_count == n (Base Case)

    # this stack will hold the parentheses
    stack = []

    # this is going to hold all the valid parentheses
    res = []

    def backtrack(open_count, closed_count):
        
        # Base Case
        if open_count == closed_count == n:
            res.append("".join(stack))
            return
        
        # if we want to add a open parentheses to the stack
        if open_count < n:
            stack.append("(")
            backtrack(open_count+1, closed_count)
            stack.pop()

        if closed_count < open_count:
            stack.append(")")
            backtrack(open_count, closed_count + 1)
            stack.pop()

    backtrack(0, 0)

    return res
        
