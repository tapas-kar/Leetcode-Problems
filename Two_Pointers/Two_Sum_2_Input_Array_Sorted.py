# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Approach 1: Approach it like Two Sum and add 1 to both the indexes
# I mean it passed 19/24 test cases, so YOU KNOW Z__\

# def twoSum(numbers: list[int], target: int) -> list[int]:

#     target_dict = {}

#     for n in numbers:
#         diff = target - n
#         print(diff)
#         if str(diff) in target_dict.keys():
#             print(f"If: {numbers.index(n) + 1, target_dict[str(diff)] + 1}")
#             return [numbers.index(n) + 1, target_dict[str(diff)] + 1]
#         else:
#             target_dict[str(n)] = numbers.index(n)
#             print(f"Else: {target_dict}")

# numbers = [2, 7, 11, 15]

# target = 9

# twoSum(numbers, target)
# Runtime: O(n)
# Space: O(1)


# Approach 2: Is how Neetcode would do it!
def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] > target:
            right = right - 1
        elif numbers[left] + numbers[right] < target:
            left = left + 1
        else:
            return [left+1, right+1]
