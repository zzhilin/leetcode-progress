class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # cnt number of nodes
        high_cnt = 0
        freq = defaultdict(int)
        graph = collections.defaultdict(list)
        for i in range(len(parents)):
            if parents[i] >= 0:
                graph[parents[i]].append(i)
        def dfs(node):

            product, size = 1, 1
            for nei in graph[node]:
                cnt = dfs(nei)
                product *= cnt
                size += cnt
                
            product *= len(parents)-size or 1
            freq[product] += 1
            return size
        dfs(0)
        return freq[max(freq)]