# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

from typing import Optional

class ListNode:
    def __init__ (self, next, val=0):
        self.next = next
        self.val = val
    


# this method is going to merge 2 sorted linked lists in 1 single linked list
def mergeSortedLinkedList(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    dummy = ListNode()

    tail = dummy

    while l1 and l2:

        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next

        tail = tail.next

    # For the case where either of the linked list is bigger than the other one
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

