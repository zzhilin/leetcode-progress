class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        TREE STRUCTURE and head
        
        """
        # build graoh
        people = defaultdict(list)
        for i, val in enumerate(manager):
            people[val].append(i)
        
        res = 0
        # dfs
        def dfs(manager_i, time):
            nonlocal res
            res = max(res, time)
            for person in people[manager_i]:
                dfs(person, time+informTime[manager_i])
            
        dfs(headID, 0)
        return res
                
        
        