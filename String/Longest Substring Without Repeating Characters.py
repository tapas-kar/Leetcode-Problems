def lengthOfLongestSubstring(s):

    # This method is by checking if the character has been added
    # Updating the start index based on repetition of characters
    # max_len, start = 0, 0
    #
    # if len(s) == 1:
    #     return 1
    #
    # for i in range(1, len(s)):
    #
    #     if s[i] in s[start:i]:
    #         start = s.index(s[i], start) + 1
    #
    #     if i - start + 1 > max_len:
    #         max_len = i - start + 1
    #
    # print(max_len)
    #
    # return max_len

    # Sliding window technique

    charSet = set()

    l = 0

    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)

    return res


s = "pwwkew"

lengthOfLongestSubstring(s)