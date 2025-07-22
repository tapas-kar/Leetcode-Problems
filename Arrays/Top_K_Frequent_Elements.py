# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Approach 1: Using a dictionary to count frequencies and then extracting the top k elements

def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter_dict = {}

    for i in nums:
        if i in counter_dict:
            counter_dict[i] += 1
        else:
            counter_dict[i] = 1

    result = []

    while k > 0:
        # Get the key with the highest frequency
        max_freq = max(counter_dict.values())
        max_keys = [key for key, freq in counter_dict.items() if freq == max_freq]

        # Add keys to result (could be multiple with same max frequency)
        for key in max_keys:
            if k > 0:
                result.append(key)
                del counter_dict[key]  # safe now because we’re not iterating over it
                k -= 1
            else:
                break

    return result

# Apperoach 2: Using a heap to find the top k frequent elements
from collections import Counter
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
