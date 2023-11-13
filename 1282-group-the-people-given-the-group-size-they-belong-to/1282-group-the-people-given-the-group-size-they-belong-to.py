class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # O(N)
        # dict size - person\
        assignments = defaultdict(list)

        res = []
        for i in range(len(groupSizes)):
            assignments[groupSizes[i]].append(i)
            if len(assignments[groupSizes[i]]) == groupSizes[i]:
                res.append(assignments[groupSizes[i]])
                assignments[groupSizes[i]] = []
        return res