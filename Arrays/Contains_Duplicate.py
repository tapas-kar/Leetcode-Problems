# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: nums = [1,2,3,1] --> Output: true
# Input: nums = [1,2,3,4] --> Output: false
# Input: nums = [1,1,1,3,3,4,3,2,4,2] --> Output: true

# BLIND 75!!

from typing import List




# APPROACH - 1 - Using a Dictionary Data Structure
# THIS IS THE DUMB WAY TO DO IT!!!
# This solved the problem, but then, the problem was that it was NOT the most efficient - Follow up: Find the run-time and space complexity of ALL the approaches


# def containsDuplicate(nums: List[int]) -> bool:
#     result = {}

#     for i in nums:
#         if i in result.keys():
#             result[i] += 1
#         else:
#             result[i] = 1
    

#     success = False
#     ans_arr = []

#     for i in result:
#         if result.get(i) > 1:
#             success = True
#             ans_arr.append(success)
#         else:
#             sucess = False
#             ans_arr.append(success)

#     if True in ans_arr:
#         return True
#     else:
#         return False




# APPROACH - 2 - Using a Set Data Structure
# HAVE YOU EVER HEARD OF SETS, YEAH USE THEM FOR DUPLICATE QUESTIONS!!!
# Whenever you see duplicate, think about Sets or Dictionary for keeping track of the duplicates

# def containsDuplicate(nums: List[int]) -> bool:
#     res = set()

#     for i in nums:
#         res.add(i)
    
#     return len(res) != len(nums)




# APPROAH - 3 - Going through each element of the Array and comparing it with every other element of the array 
# (THE DUMBEST WAY TO DO - RuntimeO(n^2))
# NOTE: Figure out how to do this the DUMB way

# def containsDuplicate(nums: List[int]) -> bool:

#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             while i != j:
#                 print("i: {} and j: {}".format(i, j))
#                 if nums[i] == nums[j]:
#                     return True
#                 else:
#                     return False




# APPROACH - 4 - Sort the Array first
# Once we sort the array, the duplicate elements are going to be close to each other
# THAT MEANS - You only have to go through the Array ONCE and compare to see if ANY ADJACENT ELEMENTS are duplicates - Use TWO POINTERS for this! - Give it a try
# Run-time - O(n)
# Space-complexity - O(1) because the sorting function WILL NOT NEED MORE SPACE (...like my gyals!)

# def containsDuplicate(nums: List[int]) -> bool:




# APPRACH - 5 - Use a HashSet (AKA Set *SMFH*) - Neetcode Preferred Solution - IDK WHY HE CALLS A SET, A haSHsEt !!?? What is that about? Anyway...
# Look up will be O(1); Run-time will be O(n) but space-complexity will also be O(n)
# Pretty similar to the set solution that I added above

def containsDuplicate(nums: List[int]) -> bool:

    result = set()

    for i in nums:
        if i in result:
            return True
        result.add(i)

    return False


# TRY THE contains duplicate II and maybe III as well? Not now, you can do it later


nums = [2,14,18,22,22]

ans = containsDuplicate(nums)

print(ans)
