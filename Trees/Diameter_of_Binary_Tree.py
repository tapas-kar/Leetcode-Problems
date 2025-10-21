# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100


# Approach 1 - My approach
# This did not work since the recursive DFS is going to return the height wrt to the root, not the diameter
# Keep in mind!!! That the diameter of the tree could be bigger than the height of the tree from the root since the left or the right subtree could have a larger subtree

# def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

#     # Basically add the max of both the left and the right subtrees

#     if not root:
#         return 0
    
#     if root:
#         return 1
    
#     left = self.diameterOfBinaryTree(root.left)
#     right = self.diameterOfBinaryTree(root.right)

#     return left + right





# Approach 2 - Neetcode's Approach
# He initializes a global variable where he stores the maximum diameter of the tree based on which node is being processed right now
# He does this because the DFS algorithm that we usually use to calculate the height of the left or the right subtree, returns the HEIGHT NOT THE DIAMETER
# The question asks us to return the MAXIMUM DIAMETER, which uses the HEIGHT calculation at each node to output the diameter but both of those are different metrics

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

    self.res = 0

    def dfs(curr):
        if not curr:
            return 0
        left = dfs(curr.left)
        right = dfs(curr.right)

        self.res = max(self.res, left + right)

        return 1 + max(left, right)
    
    dfs(root)
    return self.res