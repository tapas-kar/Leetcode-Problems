def containsDuplicate(nums):

    present = {}

    for i in range(len(nums)):
        if nums[i] in present:
            return True
        else:
            present[nums[i]] = 1
    return False


nums = [1, 2, 3, 1]

containsDuplicate(nums)
