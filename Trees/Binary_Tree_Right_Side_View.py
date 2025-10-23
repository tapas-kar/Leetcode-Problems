# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]


# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]


# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]


# Example 4:
# Input: root = []
# Output: []

 

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Approach 1 - Neetcode
# We are going to solve this doing BFS because that is the easier way to implement it
# Initially, the rightSide variable is going to be set to None and it will be updated after the node is popped from the left!! - BUT WHY FROM THE LEFT
# Trace Neetcode's algo to verify | Look at other solutions

from collections import deque

def rightSideView(self, root: Optional[TreeNode]) -> list[int]:

    res = []

    q = deque()
    q.append(root)

    while q:

        qLen = len(q)
        rightSide = None

        for i in range(qLen):

            node = q.popleft()

            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)

        if rightSide:
            res.append(rightSide.val)

    return res