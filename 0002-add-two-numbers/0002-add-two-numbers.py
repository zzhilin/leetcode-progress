# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        
        ans_d = ListNode(-1)
        ans = ans_d
        
        '''
        node can be none
        1,1,1,1
        1,1
        '''
        overflow_val = 0
        prev = False
        while p1 or p2 or overflow_val:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            curr_val = v1 + v2 + overflow_val
            
            overflow_val  = curr_val // 10
            
            digit = ListNode(curr_val % 10)
            if ans.val == -1:
                ans_d.next = digit
                ans = ans.next
            else:
                ans.next = digit
                ans = ans.next

            p1=p1.next if p1 else None
            p2 = p2.next if p2 else None

        return ans_d.next
            