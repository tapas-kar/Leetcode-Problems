# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1] --> Output: true

# Input: nums = [1,2,3,4] --> Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2] --> Output: true

from typing import List


# def containsDuplicate(nums: List[int]) -> bool:

    
#     # THIS IS THE DUMB WAY TO DO IT!!!
#     # This solved the problem, but then, the problem was that it was NOT the most efficient
    
#     result = {}

#     # print(nums)

#     for i in nums:
#         if i in result.keys():
#             result[i] += 1
#         else:
#             result[i] = 1
    
#     print(result)

#     success = False

#     ans_arr = []

#     for i in result:
#         print(i)
#         if result.get(i) > 1:
#             # print(result[i])
#             success = True
#             ans_arr.append(success)
#         else:
#             # print(result[i])
#             sucess = False
#             ans_arr.append(success)

#     if True in ans_arr:
#         return True
#     else:
#         return False

# HAVE YOU EVER HEARD OF SETS, YEAH USE THEM FOR DUPLICATE QUESTIONS!!!

# Whenever you see duplicate, think about Sets or Dictionary for keeping track of the duplicates

def containsDuplicate(nums: List[int]) -> bool:
    res = set()

    for i in nums:
        res.add(i)
    
    return len(res) != len(nums)
        

nums = [2,14,18,22,22]

ans = containsDuplicate(nums)

print(ans)

# The set approach
# res_set = set()

#         for i in nums:
#             if i in res_set:
#                 return True
#             else:
#                 res_set.add(i)
        
#         return False