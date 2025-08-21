# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Approach 1: To go through the left and right area of each combination possible between two heights
# Runtime: O(n**2)
# Space: O(1)
def maxArea(heights: list[int]) -> int:

    res = 0
    
    for l in range(len(heights)):
        for r in range(l+1, len(heights)):
            area = (r-l) * min(heights[l], heights[r])
            res = max(area, res)

    return res
# Runtime: O(n)
# Space: O(1)

def maxArea(height: list[int]) -> int:
    # the two endpoints of the ith line are (i, 0) and (i, height[i])

    # so for ex: [1,8,6,2,5,4,8,3,7]
    # that means ith endpoint is (i, 0) and (i, height of i)
    # for i = 0 --> (0,0) and (0, 1)
    # for i = 1 --> (1,0) and (1, 8)
    # for i = 2 --> (2, 0) and (2, 6)

    # endpt_tuples = []

    # for e, h in enumerate(height):
    #     endpt_tuples.append(((e, 0), (e, h)))

    # print(endpt_tuples)

    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r-l) * min(height[r], height[l])
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)
