# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 1000
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Approach 1 - Using sorting to group anagrams
# You can sort each string and use the sorted string as a key to group the anagrams
# Runtime: O(N * K log K), where N is the number of strings and K is the maximum length of a string
# Space Complexity: O(N * K), where N is the number of strings and K is the maximum length of a string

def groupAnagrams(strs: List[str]) -> List[list[str]]:
    from collections import defaultdict
    anagrams = defaultdict(list)
    for s in strs:
        # Sort the string to use as a key
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())


# Approach 2: User an array of 26 integers to count the frequency of each character
# This approach uses a tuple of character counts as the key to group anagrams

def groupAnagrams(strs: List[str]) -> List[list[str]]:
    from collections import defaultdict
    anagrams = defaultdict(list)
    
    for s in strs:
        # Create a count of characters in the string
        count = [0] * 26  # For lowercase English letters
        for char in s:
            count[ord(char) - ord('a')] += 1
        # Use the tuple of counts as a key
        key = tuple(count)
        anagrams[key].append(s)
    
    return list(anagrams.values())