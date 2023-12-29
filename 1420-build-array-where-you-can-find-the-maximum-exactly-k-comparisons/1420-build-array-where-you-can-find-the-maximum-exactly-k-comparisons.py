class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        how many arr of len n within range 1 to m inclusive can we build,
        so there are exactly k new maximums going left to right
        
        build arr:
        1. how many elements we have so far, what is next index
        2. max in arr
        3. how many remaining new maximums must we meet before end of arr
        """
        
        # recursive
        @cache
        def build(index, curr_max, remain_max) -> int:
            """
            return number of ways to build an arr if we placed index elements, max is curr_max, 
            need to place remain_max more new maximums.
            """
            
            # base
            if index == n:
                if remain_max == 0:
                    # done
                    return 1
                return 0
            # if remain_max < 0:
            #     # put too many maximum, end here
            #     return 0
            # possibilities at index
            # new element at index is not new max
            '''
            range of possible numbers is [1, maxSoFar]. There are maxSoFar possibilities in this range. By placing any of these numbers, we reach the next state dp(i + 1, maxSoFar, remain). So the total possibilities of placing a non-maximum is
            '''
            not_max = (curr_max * build(index+1, curr_max, remain_max)) % MOD
            '''
            range: curr_max + 1, m
            is max
            '''
            for i in range(curr_max+1, m+1):
                not_max = (not_max + build(index+1, i, remain_max-1)) % MOD
                
            return not_max
        
        MOD = 10 ** 9 + 7
        return build(0, 0, k)