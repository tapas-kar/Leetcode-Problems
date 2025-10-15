# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Approach 1: My attempt
# Runtime: O(n) # because it will traverse the entire tree to find the max depth
# Space: O(h) # because the recursive stack will create h frames per subtree on the left and the right

def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Recursive solution on my own without looking at the solution!!!
    # To be fair, I had actually peeped it when I asked ChatGPT about the Optional data type
    if not root:
        return 0 # I had to add a 0 because I had not added it the first time around and that gave me a comparison error on None object
    
    # recursively get the max depth of both the left and the right subtree
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return 1 + max(left, right) # 1 + the max of both sides because the root node is considered as a separate level