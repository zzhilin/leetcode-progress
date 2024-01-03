class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # backtracking recursive function takes current position in s and current list of IP segments
        def validIP(index, segments):
            
            
            
            # basecase
            # when list of ip has all 4 segments and we reach end of string, add this list to result
            if len(segments) == 4 and index == n:
                res.append('.'.join(segments))
                return
            # if we reached end of string has less than 4 segments,  backtrack
            if index == n and len(segments) < 4:
                return
            
            # iterate possible ip segments from 1 to 3 digits starting at index
            for i in range(index, min(index+3, n)):
                ip = s[index:i+1]
                # for each segment, check if it's valid (within 0 to 255 and without leading 0 unless it's 0)
                if (len(ip) > 1 and ip[0] == '0') or int(ip) > 255:
                    continue
                # if it's valid, add to list of ips and call validIP with updated index
                segments.append(ip)
                # moves to next position
                # not index +1 because index + 1 only moves by one character not moving to next segment
                validIP(i+1, segments)
                # backtrack
                segments.pop()
            
        
        res = []
        ips = []
        n = len(s)
        validIP(0, ips)
        return res