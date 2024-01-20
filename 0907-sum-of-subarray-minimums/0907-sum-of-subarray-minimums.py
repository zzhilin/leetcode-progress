class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # base case subarr len = 1
        # we can use monotonic stack to identify the range where curr element is min
        
        '''
        mono_st = [] #increasing (value, index)
        pop from stack until it's empty or curr element on top is smaller 
        [3,1]
        2 -> popped 1
        '''
        
        # find next smaller element on left and right of curr
        # at index i, next smaller on left of i is L, on right is R
        # number of subarr can be formed is (i - L) * (R - i)
        # i = 2, L = 1, R = 4 because no smaller element, so boundary is len of arr
        # num of subarr with 2 is 2, contribution to sum is 2*2
        
        stack = []
        total = 0
        n = len(arr)
        
        for i, val in enumerate(arr):
            while stack and val <= stack[-1][0]:
                popped_val, popped_i = stack.pop()
                L = stack[-1][1] if stack else -1
                R = i
                num_subarr = (popped_i - L) * (R - popped_i)
                
                contribution = num_subarr * popped_val
                total += contribution
            stack.append((val, i))
            
        while stack:
            popped_val, popped_i = stack.pop()
            L = stack[-1][1] if stack else -1
            R = n
            num_subarr = (popped_i - L) * (R - popped_i)
            contribution = num_subarr * popped_val
            total += contribution
            
        return total % (10 ** 9 + 7)