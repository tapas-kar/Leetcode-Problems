# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1: 
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false




# APPROACH 1 - Building a dictionary and comparing it with each other
# Run-time complexity: O(n)
# Space complexity: O(1)

# def isAnagram(s: str, t:str) -> bool:

#     s_dict = {}

#     t_dict = {}

#     for i in s:
#         if i in s_dict.keys():
#             s_dict[i] += 1
#         else:
#             s_dict[i] = 1

#     # print(s_dict)

#     for j in t:
#         if j in t_dict:
#             t_dict[j] += 1
#         else:
#             t_dict[j] = 1

#     # print(t_dict)

#     if s_dict == t_dict:
#         print("True")
#         return True
#     else:
#         print("False")
#         return False





# APPROACH 2 - Sort both the strings and compare them
# If they are an anagram of each other then, it will return True, otherwise False
# Run-time complexity - after sorting O(n * log (n))
# Space-complexity - O(n)

# def isAnagram(s: str, t:str) -> bool:
#     return sorted(s) == sorted(t)




# APPROACH - 3 - Whatever I am about to write down
# dict.get(x, 0) --> will prevent the code from throwing "the key does not exist" error --> 
#    # if the key is not there then, it will just return the default value, which is the 2nd argument

# def isAnagram(s: str, t:str) -> bool:
    
    # if len(s) != len(t): # If the length of one string is DIFFERENT than the other string then, it FOR SURE CANNOT BE AN ANAGRAM
    #     return False

    # countS, countT = {}, {} # Make 2 dictionaries

    # for i in range(len(s)):
    #     countS[s[i]] = 1 + countS.get(s[i], 0)
    #     countT[t[i]] = 1 + countT.get(t[i], 0)

    # # What is going on here!?!?!?
    # for char in s:
    #     if countS[char] != countT.get(char, 0):
    #         return False

    # return True





# APPROACH - 4 - Use a Python data structure called Counter and compare both the Counters for s and t strings

s = "anagram" 
t = "nagaram"

ans = isAnagram(s, t)

print(ans)