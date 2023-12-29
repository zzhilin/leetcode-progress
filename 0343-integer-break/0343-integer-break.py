class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        break down n to at least 2 numbers, maximize product of these integers
        10
        1,9
        5,5
        3,2,3,2
        
        
        7
        2,5
        3,4
        
        2,3,2
        
        i, n-i
        
        '''
        if n == 2:
            return 1
        if n == 3:
            return 2
        memo = {}
        def dp(num):
            if num == 1:
                return 1
            if num == 2:
                return 2
            if num == 3:
                return 3
            
            if num in memo:
                return memo[num]
            
            res = num
            for i in range(2,num+1):
                res = max(res, i * dp(num-i))
            memo[num] = res

            return res
        
        return dp(n)