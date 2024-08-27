# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]


# Example 3:
# Input: root = []
# Output: []

# Approach 1: The only approach as I did not know where to start
# This is a recursive solution that calls the self function "invertTree" on root.left and root.right 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):

        # the base case where if the root is None, you return None
        if not root:
            return None
        
        # store the root.left in a temp variable
        temp = root.left

        # set the left value to root's right value
        root.left = root.right

        # set the right value to the temp variable that has the root's left value
        root.right = temp


        # recursively call the invertTree function on both the root's left and right node
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return the root to get the inverted tree
        return root



    
