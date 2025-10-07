# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Approach 1: Neetcode
# First we need to use the slow and fast pointer to find the middle of the list so we can break it into 2 halves
# Then, we are going to reverse the 2nd half of the list
# Then, we are going to merge the 1st half of the list with the 2nd half of the list
# 
# Runtime: O(n)
# Space: O(1)

def renderList(head: Optional[ListNode]) -> None:
    # this is to find the middle of the linked list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Now that we have found the middle point of the list at slow, which is going to be the head of the 2nd half of the list - it is time to reverse this 2nd half
    # declaring the second half head as slow.next
    second = slow.next

    # STARTING THE REVERSAL - setting prev and the head to None
    prev = slow.next = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # Now that the reversal is done, the prev pointer contains the head of the second half of the REVERSED list
    first, second = head, prev
    # since there is a chance that the second half of the list could be shorter than the first half, we use that to check if we have merged all the elements
    # STARTING THE MERGE
    while second:
        # preserving the pointer for the iterator in the while loop to go to the next node to merge BEFORE breaking the link
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


