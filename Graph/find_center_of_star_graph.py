# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
# Example 2:

# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
 

# Constraints:

# 3 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.

# def findCenter(self, edges: List[List[int]]) -> int:

#         # total number of vertices
#         n = len(edges) + 1

#         vote = [0] * (n+1)

#         for i, j in edges:
#             vote[i] += 1
#             vote[j] += 1

#         for i in range(len(vote)):
#             if vote[i] == len(edges):
#                 return i
#         return

# Runtime: O(N)
# Space: O(N)


# # The Greedy Algorithm
# Since the center of the graph is definitely there, we can just find the one common vertex between the first and the second edges
# One of the edges from the first tuple is BOUND to have that vertex


def findCenter(self, edges: List[List[int]]) -> int:

    first_edge, second_edge = edges[0], edges[1]

    return first_edge[0] if first_edge[0] in second_edge else first_edge[1]
