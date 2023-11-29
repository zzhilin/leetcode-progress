class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        res =0
        
        first = costs[:candidates]
        last = costs[max(len(costs)-candidates, candidates):]

        heapq.heapify(first)
        heapq.heapify(last)
        
        i=candidates
        j=len(costs)-candidates-1
        
        for curr in range(k):
            if not last or first and first[0] <= last[0]:
                res += heappop(first)
                if i<=j:
                    heappush(first,costs[i])
                    i+=1
            else:
                res += heappop(last)
                if i<=j:
                    heappush(last,costs[j])
                    j-=1
        return res