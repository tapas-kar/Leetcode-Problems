class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy
            copy.neighbors += [dfs(neighbor) for neighbor in node.neighbors]
            return copy

        # remember to use "if node" to avoid edge case like []
        return dfs(node) if node else None
