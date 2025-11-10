# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

# Approach 1 - Divide the problem into sub-problems where we calculate the permututation of smaller and smaller set of numbers
# For ex: let's say we are asked to do a permutation of [1, 2, 3] -> that breaks down to let's say permutation of [2, 3] -> that breaks down to let's say permutation of [3]
# And the last base case of that would be permutation of [], which is just [], which is the base case
# Then we return from that down the call stack

# Runtime: O(n! * n^2)
# Space: O(n! * n)

def permute(self, nums: list[int]) -> list[list[int]]:
    if len(nums) == 0:
        return [[]]
    
    perms = self.permute(nums[1:])

    res = []

    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            res.append(p_copy)
    return res

# Approach 2 - Solution without recursion
# The key idea is to add each number from nums into the existing permutations that are generated in each loop
def permute(self, nums: list[int]) -> list[list[int]]:

    perms = [[]]

    for n in nums:
        new_perms = []
        for p in new_perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                new_perms.append(perms)
        perms = new_perms
    return perms