# Given a binary tree, determine if it is height-balanced.

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Approach 1 - I was close wuth the dfs and returning multiple values from the DFS

# def isBalanced(self, root: Optional[TreeNode]) -> bool:

#         def dfs(curr):
#             # get the height of both left and right sub-tree and compare their height

#             # if the height difference is 0 or 1 then return true
#             # if the height difference is more than 1 then return false

#             if not curr:
#                 return 0

#             left = dfs(curr.left)
#             right = dfs(curr.right)

#             return 1 + left, 1 + right
#         left, right = dfs(root)

#         if ((left - right) == 0) or ((left - right) == 1) or ((right - left) == 0) or ((right - left) == 1): # error here
          # error was - TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
#             return True
#         return False



# Approach 2 - Neetcode

# Runtime: O(n)
# Space: O(n), where n is the number of nodes

def isBalanced(self, root: Optional[TreeNode]) -> bool:

    def dfs(root):
        if not root:
            return [True, 0]
        
        left, right = dfs(root.left), dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]