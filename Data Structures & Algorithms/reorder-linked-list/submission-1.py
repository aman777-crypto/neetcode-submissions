# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secHead = slow.next
        slow.next = None

        prev = None
        curr = secHead
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        secHead = prev

        m1 = head
        m2 = secHead

        while m2:
            next1 = m1.next
            next2 = m2.next

            m1.next = m2
            m2.next = next1

            m1 = next1
            m2 = next2




        