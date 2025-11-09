# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

# Approach 1: Recursive DFS backtracking
# Runtime: O(2 ^ t), where t is the target and it is 2 raised to t because at every element in the candidates list, we are making 2 different choices
# that is, 1 is to include one type of combination of sum, and the other is to NOT include that same combination of sum

def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
    res = []

    # i is the iterator that is used to traverse through the candidates
    # cur is used to keep track of the current combination of candidates
    # total is used to keep track of the sum of the combination of candidates coming from cur
    def dfs(i, cur, total):

        # Base Case: We return if the total is equal to the target
        # we add the current combination's copy to res
        if total == target:
            res.append(cur.copy())
            return
        
        # Base Case 2: If the iterator is greater than or equal to the length of the candidates OR the total exceeds the target value
        # Then we return to go either end the DFS or to go back and try a different combination
        if i >= len(candidates) or total > target:
            return
        
        # If we skip over the above 2 IF conditions, that means either the total is equal to the target
        # OR the total is still under the target OR the iterator has yet to pick one of the candidates from the input

        # Then we make 2 decisions: either to include the current candidate's combination or to exclude the already included combination

        # this is where we append one of the candidates from the input list to current combination and run DFS
        cur.append(candidates[i])

        # while running DFS, we add the value of the current candidate to the total, pass in the current iterator, and pass in the current combination
        dfs(i, cur, total + candidates[i])

        # this is where we EXCLUDE the already added current combination, so we pop from the current combination
        cur.pop()

        # calling DFS on a candidate starting from a different candidate after i because for i, DFS was called above this decision
        dfs(i + 1, cur, total)

    # Call the DFS algorithm at i=0, current combination as empty array, total=0
    dfs(0, [], 0)
    return res