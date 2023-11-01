class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        RED = 2
        BLUE = 1

        colors = [0] * len(graph)

        def bfs(node):
            q = deque([node])
            colors[node] = RED

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if colors[nei] == colors[node]:
                        return False
                    if colors[nei] == 0:
                        # if colors[node] == BLUE:
                        #     colors[nei] = RED
                        # else:
                        #     colors[nei] = BLUE
                        colors[nei] = 3 - colors[node]
                        q.append(nei)
            return True

        for i in range(len(colors)):
            if colors[i] == 0:
                if not bfs(i):
                    return False
        return True

        