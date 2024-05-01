# Inorder Traversal
# This is the tree algorithm where the algorithm (it) traverses 
# the left sub-tree first, then processes the parent node, then processes the right sub-tree

class TreeNode:
    def __init__(self, root: Optional [TreeNode]) -> List[int]:
        self.val = Val
        self.left = left
        self.right = right


# Recursive solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)

        return result
