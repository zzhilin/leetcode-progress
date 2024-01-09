class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # input is nums arr of range 0, n-1
        
        max_len = float("-inf")
        INF = float("inf")
        # dp(visited) returns curr length of set s[k]
        # base case we have visited number, return and update max len
        # start from 0 to n-1, build our set and mark visited
        
        for i in range(len(nums)):
            
            
            # if curr == INF:
            #     max_len = max(max_len, length)
            #     continue
            # mark as visited
            if nums[i] != INF:
                
                curr = nums[i]
                length = 0
                while nums[curr] != INF:
                    tmp = curr
                    curr = nums[curr]
                    length += 1
                    nums[tmp] = INF
                max_len = max(length, max_len)
        return max_len