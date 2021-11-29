def maxProfit(prices):

    max_p = 0
    min_p = float('inf')

    for i in range(len(prices)):
        if prices[i] < min_p:
            min_p = prices[i]
        else:
            max_p = max(max_p, prices[i] - min_p)

    print(max_p)

    return max_p


prices = [7, 1, 5, 3, 6, 4]

maxProfit(prices)