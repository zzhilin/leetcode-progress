class Solution:
    def minDeletions(self, s: str) -> int:
        """
        AABBCCXX
        """
        freq = [0] * 26
        delete = 0
        seen_freq = set()
        for c in s:
            freq[ord(c)-97] += 1
        for i in range(26):
            while freq[i] and freq[i] in seen_freq:
                freq[i] -= 1
                delete += 1

            seen_freq.add(freq[i])
        return delete
            
                