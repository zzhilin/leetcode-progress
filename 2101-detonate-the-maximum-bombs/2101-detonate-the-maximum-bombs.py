class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """
        input list[list[int x,y,r]]
        return max detonated bombs after activate one bomb
        
        [[1,1,3],[2,2,5]]
        find longest path dfs
        build graph by calculating if another bomb is in range
        start dfs at each bomb,
        in dfs(bomb) add to visited, max count + 1, check neighbor and dfs
        """
        def in_range(b1,b2):
            x1,y1,r1 = b1
            x2,y2,r2 = b2
            return ((x1-x2)**2 + (y1-y2)**2) <= (r1**2)
        graph = defaultdict(list)
        
        
        max_count = 0
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and in_range(bombs[i], bombs[j]):
                    graph[i].append(j)
        def dfs(node,visited,count):
            visited.add(node)
            # count = 1
            for nei in graph[node]:
                # print(visited,count)
                if nei not in visited:
                    # count = max(dfs(nei,visited)+1, count)
                    # count+=1
                    count = max(count,dfs(nei,visited,count)+1)
                    
            # print('fin count', count)
            return count
        for i in range(len(bombs)):
            visited = set()
            # print('current node',i)
            max_count = max(dfs(i,visited,1), max_count)
            # print('m', max_count)
        return max_count
            
                    