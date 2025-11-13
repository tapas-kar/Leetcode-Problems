# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# Approach 1 - Recursive DFS backtracking

def generateParenthesis(self, n: int) -> list[str]:
    
    stack = []

    res = []

    def backtrack(open_count, close_count):

        if open_count < n:
            stack.append("(")
            backtrack(open_count + 1, close_count)
            stack.pop()

        if close_count < open_count:
            stack.append(")")
            backtrack(open_count, close_count + 1)
            stack.pop()

        if open_count == close_count == n:
            res.append("".join(stack))
            return
        
    backtrack(0, 0)

    return res
