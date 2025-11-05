# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true


# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true


# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?

# Approach 1: NeetCode
# Brute force solution using Recursive Backtracking - DFS
# We are basically going to go through every single character and every neighbor of that character to traverse through the given word to find the match
# Keep in mind that we cannot revisit the same character twice within our path

# Runtime: O(n * m * 4 ^ len(word))
# Explanation: Because of the brute force traversal of the board, the runtime becomes O(n * m) where n is rows and m is cols
#           That gets multiplied by the number of times the DFS call is made for each character in the target word, so Runtime becomes O(n * m * len(word)) - in other words this is the DFS call stack
#           HOWEVER, keep in mind that - for each character in the target word, we are making 4 different DFS calls in 4 directions - so the Runtime then becomes O(n * m * 4 ^ len(word))
#           or simply O(n * m * 4^n), where the 2nd "n" is the len(word)

def exist(self, board: list[list[str]], word: str) -> bool:
    # first thing is to get the length of the rows and the cols
    ROWS, COLS = len(board), len(board[0])

    # we are going to use a set to add the characters from the board that are within our path; so we don't revisit the position twice
    path = set()

    # Neetcode likes to use a nested dfs function because then he won't have to pass the board or the word variable again
    # We are going to pass in the position of the board that we are at (r, c)
    # We are also going to have to pass in a 3rd variable i, which is going to be the current character within our target word that we are looking for
    def dfs(r, c, i):

        # if we ever reach the end of the word, that is, i is equal to the last position of the word
        # this is the "Good case" or the Base Case
        if i == len(word):
            return True
        
        # Next case is when do we return False, there are multiple conditions to look out for:
        # if the row < 0 OR col < 0
        # OR if the row >= actual number of rows OR if the col >= actual number of cols
        # OR if the current character on our board position is NOT equal to the current character in our target word
        # OR if the current position on our board (r, c) is already visited and added to the path set
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
            return False
        
        # If the above IF condition is not hit then, that means that we have found a character on the board that is in our target word, so we can continue our DFS
        # Hence, we add that (r, c) position from the board to our path
        path.add((r, c))

        # we are going to be looking for the result of this DFS
        # keep in mind that when we run this DFS, we are going to be running this in all 4 adjacent positions
        # In the result, we add i+1 because if the 2 IF conditions get skipped then, that means we have found a character that is part of the target word BUT...
        # we are NOT done with the DFS yet, so run the DFS algo on the next character in the target word
        res = (dfs(r + 1, c, i+1) or dfs(r - 1, c, i+1) or dfs(r, c + 1, i+1) or dfs(r, c - 1, i+1))
        
        # we add this to clean up the path set because we don't NEED to visit that (r, c) position anymore
        path.remove((r, c))

        # we return res - that means if any of the dfs calls from res above return True, we return True, otherwise it would automatically return False
        return res
    
    # Note: The above DFS is always the main part of any Backtracking problem

    # Brute force: Run the above DFS function on every single starting position on the board
    for r in range(ROWS):
        for c in range(COLS):
            # again keep in mind that the i variable in the above DFS signifies the index of where we are in the target word
            # so we call the DFS function starting from the beginning of the target word to match characters on the board at position (r, c)
            if dfs(r, c, 0): 
                return True
    return False
