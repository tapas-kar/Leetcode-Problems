# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

# Approach 1: My Approach - Passed 14/49 test cases!! That is insane
# def characterReplacement(s: str, k: int) -> int:


#     window = []
#     window.append(s[0])

#     l = 0

#     switch_count = 0

#     max_length = 0

#     for r in range(1, len(s)):
#         if s[r] == window[-1]:
#             window.append(s[r])
#             max_length = max(max_length, len(window))
#         else:
#             if switch_count < k:
#                 s[r] = window[-1]
#                 switch_count += 1
#                 window.append(s[r])
#                 max_length = max(max_length, len(window))
#             else:
#                 l += 1
#     return max_length

# Approach 2: Neetcode
# Runtime: O(26 * n)
# Space: O(n)
def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res

# Approach 3: Neetcode with maxf optimization
def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        # instead of checking the entire dictionary for all 26 values, you can maybe check if the addition of the most recent character above cause the maxf to change
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res