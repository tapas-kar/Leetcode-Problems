# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000

# this is how to declare an Object class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        
        # This is the 2-pointer method
        # you are setting the current pointer to head and a previous pointer to None before the head
        current = head
        prev = None

        # while the current pointer is NOT NONE
        while current:
            # store the current.next value in a temp variable to access it for when you have to move your current pointer later to reverse the link
            nxt = current.next

            # you set the current's next node to prev
            current.next = prev

            # you set the previous pointer to current
            prev = current

            # you set the current pointer to the current's next that you stored earlier for another reversal of link
            current = nxt

        # return the head value for the complete reversed linked list
        return prev
