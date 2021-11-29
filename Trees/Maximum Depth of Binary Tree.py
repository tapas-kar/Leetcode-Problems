class TreeNode:
    def __init__(self, val=0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode):

        if not root:
            return 0

        # print(1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = [3, 9, 20, None, None, 15, 7]

solution1 = Solution()

answer = solution1.maxDepth(root)

print(answer)
