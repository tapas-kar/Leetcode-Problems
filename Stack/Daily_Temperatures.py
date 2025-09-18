# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

# Example 1:

# Input: temperatures = [30,38,30,36,35,40,28]

# Output: [1,4,1,2,1,0,0]
# Example 2:

# Input: temperatures = [22,21,20]

# Output: [0,0,0]
# Constraints:

# 1 <= temperatures.length <= 1000.
# 1 <= temperatures[i] <= 100

# Attempt 1 -> 2 pointer approach - WRONG
# def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = []

#         i = 0
#         j = i + 1
#         for _ in range(len(temperatures)):
#             if temperatures[j] > temperatures[i]:
#                 res.append(j-i)
#             else:
#                 while i < len(temperatures) and j < len(temperatures) and temperatures[j] < temperatures[i]:
#                     j += 1
#                 res.append(j-i)
#                 i = j
#                 j = i+1

#         return res

# Attempt 2 -> Stack approach\
def dailyTemperatures(temperatures: list[int]) -> list[int]:

    # initialize everything to 0
    res = [0] * len(temperatures)

    # maintain a stack where we store pairs of values for the temperature and the index of that temperature in the input array
    stack = [] # pairs: [temp, index]

    for i, t in enumerate(temperatures): # Remember enumerate returns the index first and then the value at the index
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])
    return res



