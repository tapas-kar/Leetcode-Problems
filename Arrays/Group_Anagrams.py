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

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Approach 1 - Using a hashmap to group anagrams
# You can use a dictionary to group the anagrams together. The key will be the sorted version of the string, and the value will be a list of strings that are anagrams of each other.


def groupAnagrams(strs: List[str]) -> List[list[str]]:
    from collections import defaultdict
    anagrams = defaultdict(list)
    for s in strs:
        # Sort the string to use as a key
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

# Approach 2 - 