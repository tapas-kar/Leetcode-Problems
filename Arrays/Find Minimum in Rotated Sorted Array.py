# O(n) solution is
# def findMin(self, nums: List[int]) -> int:
#         return min(nums)

# O(log n) attempt
def findMin(nums):

    low = 0
    high = len(nums) - 1
    res = nums[0]

    while low < high:

        if nums[low] < nums[high]:
            res = min(res, nums[low])
            break
        mid = (high + low) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[low]:
            low = mid + 1

        else:
            high = mid - 1

    return res


nums = [3, 4, 5, 1, 2]
findMin(nums)

# len is 5
# 5 // 2 = 2
# 0   1   2   3     4
# 3,  4,  5,  1,    2
# low    mid       high
#             low  high
#             mid

# 3 + 4 = 7 // 2 = 3
