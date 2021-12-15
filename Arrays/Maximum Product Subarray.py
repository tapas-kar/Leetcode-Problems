def maxProduct(nums):

    res = max(nums)

    curMin, curMax = 1, 1

    for i in nums:
        tmp = curMax * i
        curMax = max(i * curMin, i * curMax, i)
        curMin = min(i * curMin, tmp, i)

        res = max(res, curMax)

    return res




nums = [-2]

maxProduct(nums)