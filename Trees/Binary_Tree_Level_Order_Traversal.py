# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# Approach 1 - Wrote the function in one attempt, did not account for a the none case at the beginning and had to hard code it

from collections import deque

def levelOrder(self, root: Optional[TreeNode]) -> list[int]:

    if not root:
        return []
    
    res = []

    q = deque()

    q.append([root])

    while q:

        qLen = len(q)
        level = []

        for i in range(qLen):

            node = q.popleft()

            if node:
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        res.append(level)

    return res






# Approach 2 - Neetcode's solution
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        # we use a queue to implement BFS
        q = collections.deque()

        # we initialize the queue with the root that has been given
        q.append(root)

        # Now, we can start running the BFS algo
        while q:

            # this lenghth is going to make sure that we traverse the tree Level-by-Level
            qLen = len(q)

            # for each level, we need this array to store each value of the nodes as we traverse them    
            level = []

            # we loop over all the elements in the queue by level
            for i in range(qLen):

                # pop that node from the left and add it to level
                node = q.popleft()

                # we need to ensure that the node that we just popped is NOT NULL
                if node:
                    
                    # after we confirm that the node that we are adding to the level is not a NULL node, we add it to the levels array
                    level.append(node.val)
                    
                    # keep in mind that we also have to check if the node that just got added to the level array also has any child nodes, because if it does then we have to add that to the queue for further traversal
                    q.append(node.left)
                    q.append(node.right)
            
            # we check that the level array is not NULL before adding it to our result array
            if level:
                res.append(level)
        return res
