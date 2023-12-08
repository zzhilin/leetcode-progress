# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            dummy = ListNode(-1)
            prev = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    prev = prev.next
                    l1 = l1.next
                else:
                    prev.next = l2
                    prev = prev.next
                    l2 = l2.next
            if not l1:
                prev.next = l2
            else:
                prev.next = l1
            return dummy.next
        # save first list to merge in res
        
        # start at second list, we merge it with res
        
        # combine l1 and l2
        # dummy node <- prev
        # if node in l1 is smaller or equal to node in l2, point prev to l1, increment, else l2
        # repeat until one list ends. append rest to the result list
        res = None
        if len(lists)>0:
            res = lists[0]
            for i in range(1,len(lists)):
                res = merge(res, lists[i])
        return res
            
        
        