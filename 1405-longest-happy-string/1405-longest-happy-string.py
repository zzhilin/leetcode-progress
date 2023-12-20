class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # max heap like (a, 1), (b,1), (c,7)
        # add highest freq element to result str first until there are two consecutive elements
        # add different element
        cnt = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        max_h = []
        for i in cnt:
            if i[0] != 0:
                heapq.heappush(max_h, i)
        
        res = ''
        while max_h:
            cnt, item = heapq.heappop(max_h)
            if len(res) >= 2 and res[-1] == res[-2] == item:
                # dups
                if not max_h:
                    # cannot add any other str
                    break
                cnt2, item2 = heapq.heappop(max_h)
                res += item2
                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(max_h, (cnt2, item2))
            else:
                res += item
                cnt += 1
            if cnt != 0:
                heapq.heappush(max_h, (cnt, item))

        return res
        