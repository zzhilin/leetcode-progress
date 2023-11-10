class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = {}
        num_created = 0
        for pair in dominoes:
            if pair[0] < pair[1]:
                num_created = 10*pair[0] + pair[1]
            else:
                num_created = 10*pair[1] + pair[0]
            if num_created in counts:
                counts[num_created] += 1
            else:
                counts[num_created] = 1
        res = 0
        for num, cnt in counts.items():
            res += (cnt * (cnt-1)) // 2
        return res