# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Runtime: O(n) - it would be O(2n) because at each node we are comparing the value of the node with an upper bound and a lower bound that is passed down from the parent node
# Space: O(n)

# Approach 1 - NeetCode


def isValidBST(self, root: Optional[TreeNode]) -> bool:

    def valid(node, left, right):
        if not node:
            return True # because technically, an empty BST is still a BST
        
        if not ((node.val > left) and (node.val < right)):
            return False
        
        return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
    
    return valid(root, float("-inf"), float("inf")) # call the recursive DFS function, NOT the isValidBST function because the comparisons are happening in the valid function
