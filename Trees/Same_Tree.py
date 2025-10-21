# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# Runtime: O(n)
# Space: O(n)
# Well because of the question, you have to check all the nodes of both the trees, until we find there is something different in the nodes or the structure

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    # Base case: When both the trees are Null, then return True
    if not p and not q:
        return True
    
    # Base case: if one of the trees is Null or let's say both of the trees have a node but their VALUES are different then, return False 
    if not p or not q or p.val != q.val:
        return False
    
    # if neither of the above conditions are hit, that means:
    # both the trees are Non-empty, both of their roots have the same value
    # so it is time to run the DFS traversal on both the left and the right subtrees
    return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    