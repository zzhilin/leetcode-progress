class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        pos = defaultdict(int) #row: pos
        for i in range(len(bank)):
            for j in range(len(bank[0])):
                if bank[i][j] == "1":
                    pos[i]+=1
        # print(pos)
        
        rows = list(pos.keys())
        if len(rows) <= 1:
            return res
        for i in range(len(rows)-1):
            res += pos[rows[i]] * pos[rows[i+1]]
        
        return res