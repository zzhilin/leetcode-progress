class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        """
        
        """
        graph = collections.defaultdict(list)
        for x,y in paths:
            graph[x].append(y)
            graph[y].append(x)
        plant_type = {i: 0 for i in range(1,n+1)}
        
        for g in graph:
            all_flowers = set(range(1,5))
            for nei in graph[g]:
                # Mark the color as used if neighbor has used it before.
                if plant_type[nei] != 0 and plant_type[nei] in all_flowers:
                    # remove existed flower
                    all_flowers.remove(plant_type[nei])
            plant_type[g] = all_flowers.pop()
            
        res = []
        for x in range(1, n+1):
            if plant_type[x] != 0:
                res.append(plant_type[x])
            else:
                res.append(1)
        return res
                    
            