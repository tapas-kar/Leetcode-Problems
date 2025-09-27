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
        
        # ITERATIVE SOLUTION - most optimal
        # Runtime: O(n)
        # Space: O(1)
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
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # RECURSIVE SOLUTION
        # Runtime: O(n)
        # Space: O(n)

        # Best way to think about recursive problems is to break it down into sub-problems
        # Think about how to break down the problem, first the head is at the 1 Node in 1 --> 2 --> 3 --> Null
        # When using the recursive approach, we are going to ignore the head and first think about how to reverse the remaining linked list of 2 --> 3 --> Null
        # Next, we are going to think about how to reverse the remaining linked list of 3 --> Null
        # Next, we are going to think about how to reverse the remaining linked list of Null, BUT Null is not a valid node, so that brings us to our BASE CASE
        # How do we do it? Can we take the next pointer of 3 in 3 --> Null and set it to previous to 2 in 2 --> 3 --> Null???
        # NOOOOO, because 2 is not part of the sub-problem as of right now
        # SO, technically, 3 pointing to Null is considered "REVERSED" because in this current sub-problem, where we are just trying to reverse 3, the next pointer is already pointing to Null
        # After that, the next sub-problem is to reverse 2 --> 3 --> Null and NOW!! We have access to 2 to be able to set 3's previous pointer to 2 in 2 --> 3 --> Null
        # So, we set 3's next pointer to previous, which is 2 and we set 2's next pointer to Null, SO it looks like this - Null <-- 2 <-- 3
        # After than, the next sub-problem is to reverse 1 --> 2 --> 3 --> Null
        # So, we set 2's next pointer to previous, which is 1 and we set 1's next pointer to null, SO it looks like this - Null <-- 1 <-- 2 <-- 3

        # Base Case
        if not head:
            return None
        
        newHead = head
        if head.next: # that means if head.next is not None, that means there is more sub-problems to solve
            newHead = self.reverseList(head.next)
            # reversing the link between the next node and head
            head.next.next = head
        head.next = None

        return newHead

