# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3

# Approach 1: start with the first number and compare it with the 2nd number
# if the difference is + or - 1 then add the first number and shift the pointer from the 1st number to the 2nd number

# Runtime Complexity: O(n)
# Space Complexity: O(n)

def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest