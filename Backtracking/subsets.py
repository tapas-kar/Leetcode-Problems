# 78. Subsets

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]

# Approach 1: Recursive Backtracking solution
# Basically, At every element of the input array, we have a choice to either 
# 1. include that element in the subset OR 2. NOT include that element in the subset and we use a Recursive backtracking to implement that

# Runtime: O(n * (2^n))
# Space: O(n)

def subsets(nums: List[int]) -> List[List[int]]:

    result = []

    subsets = []

    def dfs(i):
            
        # Base case
        if i >= len(nums):
            result.append(subsets.copy())
            return
    
        # Decision to include the current number
        subsets.append(nums[i])
        dfs(i+1)

        # Decision to NOT include the current number
        subsets.pop()
        dfs(i+1)

    dfs(0)

    return result