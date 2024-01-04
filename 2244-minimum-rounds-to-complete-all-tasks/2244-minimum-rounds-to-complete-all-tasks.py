class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        
        res = 0
        for c in cnt.values():
            if c == 1:
                return -1
            else:
                res += ceil(c / 3)
        return res