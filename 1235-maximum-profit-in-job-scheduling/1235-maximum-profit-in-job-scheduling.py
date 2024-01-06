class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[0])
        sorted_start_times = [x[0] for x in jobs]
        
        
        
        def find_max(curr, memo):
            if curr == len(jobs):
                return 0
            if curr in memo:
                return memo[curr]

            idx = bisect_left(sorted_start_times, jobs[curr][1])

            res = max(find_max(idx, memo) + jobs[curr][2], find_max(curr+1, memo))
            memo[curr] = res
            return memo[curr]
        
        
        return find_max(0, {})
        