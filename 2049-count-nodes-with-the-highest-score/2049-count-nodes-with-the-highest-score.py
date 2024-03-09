class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        #init graph
        #use defaultdict to keep track of all scores for the number of nodes with highest scores
        graph = collections.defaultdict(list)
        scores = collections.defaultdict(int)
        for i in range(len(parents)):
            graph[parents[i]].append(i)
        
        # depth firs search for all nodes' sizes and scores
        def dfs(node):
            product, size = 1, 1
            for nei in graph[node]:
                nei_size = dfs(nei)
                # multiply product with child subtree sizes
                product *= nei_size
                size += nei_size
            # multiply product with other subtrees not connected to node
            product *= len(parents) - size or 1
            scores[product] += 1
            return size
        
        dfs(0)
        return scores[max(scores)]