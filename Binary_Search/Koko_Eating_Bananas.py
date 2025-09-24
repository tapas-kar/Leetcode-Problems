# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

# Approach 1: Neetcode Approach
# Runtime: O(n * log m) where n is the size of the input array and m is the maximum value in the array

import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles) # right pointer is at the max(piles) because if k is chosen to be max(piles) then Koko can eat that all the piles within the given h hours

    # Keep in mind that the input hours h is always going to be greater or equal to the len(piles) ensuring that there is always a valid k answer

    res = r # we're calling it res but it is really k and setting it to r because the search space is going to be from 1...max(piles)

    while l <= r:

        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
    return res
