# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(-1)
        d.next = head
        
        # len
        p = head
        l = 0
        while p:
            p = p.next
            l += 1
            
        steps = l - n
        prev=d
        while steps:
            prev = prev.next
            
            steps -= 1
        # print(prev)
        prev.next = prev.next.next
        
        return d.next