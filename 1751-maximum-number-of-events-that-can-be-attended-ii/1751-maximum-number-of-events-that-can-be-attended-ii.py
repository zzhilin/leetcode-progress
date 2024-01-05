class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [start for start, end, val in events]
        # we initialize dp arr for number of events left to attend, and current event index
        dp = [[-1] * n for _ in range(k+1)]
        def find_max_val(curr, cnt):
            '''
            return max val at curr index
            n: number of events
            '''
            if cnt <= 0 or curr >= n:
                return 0
            if dp[cnt][curr] != -1:
                return dp[cnt][curr]
            # nxt
            # find nxt event that is closest to curr with binary search
            idx = bisect_right(starts, events[curr][1])
            # attend curr meeting, nex meeting is i, used k by one
            # don't attend current meeting
            res = max(find_max_val(idx, cnt-1) + events[curr][2], find_max_val(curr + 1, cnt))
            dp[cnt][curr] = res
            return dp[cnt][curr]
        
        
        
        return find_max_val(0, k)