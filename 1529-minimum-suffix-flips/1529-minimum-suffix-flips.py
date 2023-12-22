class Solution:
    def minFlips(self, target: str) -> int:
       
        res = 0
        # in determining the true value of the current bit, we only care about the number of flips that have already occurred. If this number is odd then the value of that bit is flipped. Otherwise it is unchanged.
        # Flips cancel each other out. Instead of asking how many flips it takes to get from 0 to the target, let's ask how many flips it takes to get from the target to 0. Whenever the true value of a bit is not equal to zero, we simply add a flip.

        for bit in target:
            if res % 2 == 0:
                # if we haven't flip this bit yet
                if bit != '0':
                    # not 0 meaning we need to change to 1 and flip once
                    res += 1
            else:
                tmp = int(bit)
                if not tmp != 0:
                    # with '10111''s 0, we flipped twice to get back to 0
                    res += 1
        return res
                
        
        