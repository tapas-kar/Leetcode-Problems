# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

# Approach 1 - NeetCode approach from Combination Sum 1 and 3 Sum
# Apparently, the way to exclude duplicate elements in a combination is similar to 3 Sum, we just do it recursively for this problem


def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
    res = []
    candidates.sort()

    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        
        if total > target or i == len(candidates):
            return
        
        curr.append(candidates[i])
        dfs(i + 1, curr, total + candidates[i])
        curr.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        dfs(i + 1, curr, total)
    dfs(0, [], 0)
    return res
