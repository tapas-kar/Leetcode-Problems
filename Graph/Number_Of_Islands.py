# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from typing import List

# Approach 1: Using Breadth First Search (which is iterative and NOT recursive)
# Time complexity: O(m * n)
# Space complexity: O(m *n)

def numIslands(grid: List[List[str]]) -> int:

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    visited = set()

    total_islands = 0

    def bfs(r, c):

        q = collections.deque()

        visited.add((r, c))
        q.append((r, c))

        while q:

            row, col = q.popleft()

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:

                r, c = row + dr, col + dc

                if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    q.append((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                total_islands += 1

    return total_islands


# Here is what I learned:
# - do input validation first in case there is nothing in the grid
# - get the total number of rows and columns
# - define a variable to return for total number of islands
# - define a set that will hold all the tuples of each grid element that has been visited
# - Then, go through each of the element in the grid and check if the element is 1 AND if the element is already visited that is a 1
# - If not then, do a BFS on that particular "1" element
# - Once the BFS for that particular 1 is done, it will return to the main driver block of the code and increment the total number of islands
# - return the total number of islands in the function
# - The main part of this problem lies in how to write the BFS algortihm (again, which is iterative NOT recursive)


# BFS:
# - For the BFS algorithm, here is how we can write it
# - First we should know that BFS will use memory and that will be handled by a data structure called queue (OR deque)
# - From the driver code if you remember, BFS is run only when we encounter a grid element 1 which has not been visited yet and that BFS takes a row and a column parameter (bfs(r, c))
# - That means the current (r, c) tuple has not been visited yet, so we need to add it to the visited set
# - Then, we need to add it to the deque so that BFS can be done on that (r, c) tuple
# - Now, while the deque is not empty, that means there are more unvisited 1s in the deque that we need to run BFS on
# - Define the directions you are allowed to look at neighbors (which is down, up, right, left)
# - Loop over the directions and look for neighbors for each of the (row, col) that has just been popped from the deque
# - Check if the neighbor is in bounds of the rows and columns dimensions, if the neighbor is a "1" and if it not in visited set already
# - If all the above criteria get satisfied then, add that neighbor to the visited because it just now made it into the if block and add that 1 to the deque for further BFS


#DFS:
# - If you want to implement the DFS way then, instead of popping the earliest added element in the deque (popleft), just pop the most recent element added to the deque


# Related tip: Remember, there is a recursive way to do this problem using DFS. From Backtracking problem of finding subsets, we learned that while defining recursive DFS:
# We take the most basic base case, which will definitely return in case an index goes out of bound or something similar