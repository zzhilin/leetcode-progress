# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = n
        
        d = ListNode(-1)
        d.next = head
        p1, p2 = d, d
        
        while count:
            p1 = p1.next
            count -= 1

        
        while p1.next:
            p1 = p1.next
            p2 = p2.next

            
        p2.next = p2.next.next
        return d.next