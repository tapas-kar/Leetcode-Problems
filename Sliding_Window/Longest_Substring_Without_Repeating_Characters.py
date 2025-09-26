# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Approach 1: My approach, after some debugging on Leetcode environment
# def lengthOfLongestSubstring(s: str) -> int:

#     cur_window = "" # this needs to be a set - cur_window = set()

#     res = 0

#     l, r = 0, 0

#     while l < len(s) and r < len(s) and l <= r:

#         if s[r] not in cur_window:
#             cur_window.join(s[r]) # this was not actually joining anything to the string -- this would get added to the set - cur_window.add(s[r])
#             res = max(res, len(cur_window))
#             r += 1
#         else:
#             l += 1
#     return res

# Approach 2: Neetcode Approach
# Runtime: O(n)
# Space: O(n)

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    
    l = 0

    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        # since r is in the for loop and starts with 0 until the length of s
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
