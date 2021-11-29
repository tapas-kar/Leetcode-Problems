def productExceptSelf(nums):

    # Time Limit Exceeded
    # answer = []
    # product = 1
    #
    # for index_c, num in enumerate(nums):
    #     for j in range(len(nums)):
    #         if index_c != j:
    #             # print(index_c, j)
    #             product = product * nums[j]
    #
    #     answer.append(product)
    #     product = 1


    # O(n) attempt
    answer = [1] * len(nums)

    prefix = 1

    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer


nums = [-1, 1, 0, -3, 3]

productExceptSelf(nums)

"""
- multiply each element except for the current element
- place the product in the current index of answer

"""