# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:
# Input: prices = [10,8,7,5,2]
# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.


# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100



#APPROACH 1: The dumb approach, this is what I think!

# def maxProfit(prices) -> int:

#     current_profit = 0

#     max_profit = 0

#     i = 0

#     left, right = 0

#     while right < len(prices):

#         # if left > right then, move both left and right pointer by 1
#         # if left <= right then, move the right pointer by 1, keep the left pointer the same
#         current_profit = right - left




# Approach 2: This is Neetcode's approach for the solution
def maxProfit(prices) -> int:

    l, r = 0, 1
    max_profit = 0

    while r < len(prices):

        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    
    return max_profit

        


prices = [10, 1, 5, 6, 7, 1]

maxProfit(prices)
