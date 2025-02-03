# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n: int) -> int:

    # first we define the base cases where it is easy to solve this problem for initial decisions
    ways = {1 : 1, 2 : 2}


    # then we go from the next number upto 1 above the input n because range(n+1) only includes number upto n technically
    for i in range(3, n+1):

        # this is the pattern we notice when we do this algorithm for 3 stairs, 4 stairs, 5 stairs etc.
        ways[i] = ways[i-1] + ways[i-2]


    # this is what we need to return
    return ways[n]