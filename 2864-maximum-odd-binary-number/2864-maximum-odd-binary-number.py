class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count('1')
        n = len(s)
        
        return '1' * (one_count-1) + '0' * (n-one_count) + '1'
            
                
            