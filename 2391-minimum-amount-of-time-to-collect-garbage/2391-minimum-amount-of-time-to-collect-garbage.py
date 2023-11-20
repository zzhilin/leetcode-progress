class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cumulative_travel = [0]
        for t in travel:
            cumulative_travel.append(cumulative_travel[-1]+t)
        last = {'G': 0, 'P': 0, 'M': 0}
        cnt = {'G': 0, 'P': 0, 'M': 0}
        for i,g in enumerate(garbage):
            for type in 'GPM':
                cnt[type] += g.count(type)
                if type in g:
                    last[type] = i
        total_time = 0
        for type in 'GPM':
            total_time += cnt[type] + cumulative_travel[last[type]]
        return total_time