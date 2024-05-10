# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]


# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Example 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]

# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.




# Approach 1: The dumb approach. This is dumb because first off - It did not pass all the test cases on Leetcode and second off - the run time is n^2
# Run-time complexity: O(n^2)
# Space complexity: O(n)

# def twoSum(nums, target):

#     output = []

#     for i in range(len(nums)):

#         ind1 = target - nums[i]

#         for j in range(i+1, len(nums)):

#             print(i, j)

#             if nums[j] == ind1:

#                 output.append(i)
#                 output.append(j)

#     # print(output)

#     return output





# Approach 2: Look up the solution atp!
# The hash-map solution algo: 
# You will start the solution with an empty hashmap
# Then, you will iterate over the nums array
# For every iteration, you will check if the difference between the current value of index in nums array and the target exists in the hashmap
#     If it does then, return the pair of indexes that add up to the target sum
#     If it DOES NOT then, add that current value's index in the nums array and the current value itself as a (key, value) pair to the hashmap
# By the time the algorithm iterates over all the elements in nums array, you should find the solution at the 2nd number that adds up to the target (NEVER FIRST!!)
# This happens because we are going to sequentially add all the values' indexes and the values from nums; so, every time we hit the 2nd part of the target sum, the first part of the sum should always already be there

# def twoSum(nums, target):

#     map = {}

#     for i, n in enumerate(nums):

#         diff = target - n

#         if diff in map:
#             return [i, map[diff]]

#         map[n] = i


nums = [2, 7, 11, 15]

target = 9

twoSum(nums, target)
