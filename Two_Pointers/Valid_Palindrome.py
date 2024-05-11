# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# APPROACH 1: My approach, probably going to be dumb so just give it a try. You already know it is supposed to use 2 pointers
# IT WORKED!!!!

def isPalindrome(s: str) -> bool:

    print(len(s))

    # Before anything, clear the string of any non-alphanumeric characters
    s = ''.join(filter(str.isalnum, s)).lower()
    print(s)
    print(len(s))
    
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


s = "race a car"

isPalindrome(s)
