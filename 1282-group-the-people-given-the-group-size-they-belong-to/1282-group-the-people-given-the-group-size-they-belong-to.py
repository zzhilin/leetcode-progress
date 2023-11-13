class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # O(N)
        # dict size - person\
        assignments = defaultdict(list)
        for i in range(len(groupSizes)):
            assignments[groupSizes[i]].append(i)
        res = []
        for size, people in assignments.items():
            if size == len(people):
                res.append(people)
                continue

            for i in range(0,len(people),size):
                res.append(people[i:i+size])
        return res