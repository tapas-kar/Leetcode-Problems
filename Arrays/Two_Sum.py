def twoSum(nums, target):

    map = {}

    for i, n in enumerate(nums):

        diff = target - n

        if diff in map:
            return [i, map[diff]]

        map[n] = i


nums = [2, 7, 11, 15]

target = 9

twoSum(nums, target)