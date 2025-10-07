# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# One of the approaches to solve this would be to reverse the list, calculate n spaces from the end, set a pointer before that and delete the resulting node
# But we don't have to reverse the list to be able to solve this
# We can use a 2 pointers approach where the right pointer is shifted exactly n spaces from the beginning and keep shifting both left and right
# That way, when the right pointer reaches the end of the list, we know that the left pointer would be exactly n spaces behind that, which is the node that we need to delete
# One issue though is that because we are going to delete the node at the left pointer, we have to delete it by referecing the node that comes before that
# In order to solve for the above issue ^, we can initialize the left pointer at the dummy node

# Runtime: O(n)
# Space: O(1)

def removeNthFromEnd(head: Optional[ListNode], n: int) -> ListNode:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next