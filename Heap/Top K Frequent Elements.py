def topKFrequent(nums, k):

    count = {}

    out_arr = []

    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    for n in range(k):
        out_arr.append(sorted_count[n][0])
        print(sorted_count[n])

    return out_arr


nums = [1, 1, 1, 2, 2, 3]

k = 2

topKFrequent(nums, k)