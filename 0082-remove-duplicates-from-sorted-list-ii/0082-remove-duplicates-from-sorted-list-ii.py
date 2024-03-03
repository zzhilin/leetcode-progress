# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(-1)
        p = d
        p1 = head
        
        

        while p1:
            if p1.next and p1.val == p1.next.val:
                while p1.next and p1.val == p1.next.val:
                    p1 = p1.next
                p1 = p1.next
                if not p1:
                    p.next = None
            else:
                p.next = p1
                p = p.next
                p1 = p1.next
        return d.next
    # 1 2 3 3
    #         1
    #
    # 0 -> 1 -> 2
    #           p