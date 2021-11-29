class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None

        while head:

            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        return prev

    head = [1, 2, 3, 4, 5]

    reverseList(head)