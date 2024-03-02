# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dummy heads for less than x list and greater than x list
        d1, d2 = ListNode(-1), ListNode(-1)
        p1, p2 = d1, d2
        
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p = p.next
                p1 = p1.next
                p1.next = None
            else:
                p2.next = p
                p = p.next
                p2 = p2.next
                p2.next = None
                
        p1.next = d2.next
        return d1.next