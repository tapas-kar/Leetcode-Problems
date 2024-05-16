# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.




# Approach 1: This is my approach

def search(nums: List[int], target: int) -> int:

    # KEEP IN MIND: The part where it is sorted is VERY VERY VERY IMPORTANT for Binary Search to work as it depends heavily on sequence (asc or desc)
    # If the numbers are NOT sorted then, you cannot compare the target value with any indexes in the input array

    # There are usually 3 pointers in binary search, Left, Middle, and Right

    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        # For some interviews, you might get a weird integer value where the result of (l + r) // 2 is an Integer but the memory used to store that
        # might overflow for languages like Java, or C++
        # To avoid this small little bug, we can set the middle pointer to be exactly halfway between r like so, (r - l) // 2
        # and once we get a True integer value from the calculation, add that integer to the left pointer to find the TRUE midway point
        
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m

    return -1 


nums = [-1,0,3,5,9,12]

target = 9

print(search(nums))
