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
# Space: O(h) # because the recursive stack will create h frames per subtree on the left and the right, which could be O(n) if it is not a balanced BT

def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Recursive solution on my own without looking at the solution!!!
    # To be fair, I had actually peeped it when I asked ChatGPT about the Optional data type
    if not root:
        return 0 # I had to add a 0 because I had not added it the first time around and that gave me a comparison error on None object
    
    # recursively get the max depth of both the left and the right subtree
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return 1 + max(left, right) # 1 + the max of both sides because the root node is considered as a separate level






# Approach 2: Neetcode BFS (for no reason but just learning purposes)
# Runtime and Space complexity stays the same

from collections import deque
def maxDepth(self, root: Optional[TreeNode]) -> int:

    if not root:
        return 0
    
    level = 0

    q = deque([root]) # another way of initializing the deque with the root, wonder why it is initialized as a list though

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1

    return level





# Approach 3: Neetcode Iterative DFS
# We are doing a pre-order traversal using DFS because it is the easiest to implement - where we process the root node first and add its child nodes to the stack

def maxDepth(self, root: Optional[TreeNode]) -> int:

    # Neetcode had this earlier in the explanation with res initialized to 1 but decided to remove it because...
    # the if condition to check if the node is a Null Node or not updates the res count accordingly
    # if the node is null, the while loop executes and that null node is popped but because the "if node" condition checks if the node is null or not prevents that loop from updating the depth (res) value
    # if not root:
    #     return 0
    # res = 1
    
    stack = [[root, 1]]

    res = 0

    while stack:

        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, 1 + depth])
            stack.append([node.right, 1 + depth])

    return res