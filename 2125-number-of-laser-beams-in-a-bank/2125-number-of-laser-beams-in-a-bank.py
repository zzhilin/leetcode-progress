class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for i, beams in enumerate(bank):
            cnt = beams.count('1')
            if cnt == 0:
                continue
            if not prev:
                prev = cnt
                continue
                
            else:
                res = res + (prev * cnt)
                prev = cnt
        return res