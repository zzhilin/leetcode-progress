class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        end = 10
        if len(s) < 10:
            return []
        dna = {}
        res = []
        start = 0
        while end < len(s)+1:
            curr = s[start:end]
            if curr not in dna:
                dna[curr] = 1
            else:
                if curr not in res:
                    res.append(curr)
            start += 1
            end += 1
        return res