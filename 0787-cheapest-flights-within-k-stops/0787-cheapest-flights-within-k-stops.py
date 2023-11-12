class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        input: flights[from, to, price] int, src, dst, k
        return lowest price src to dst most k stops / -1
        
        """
        
        graph = defaultdict(list)
        prices = [10000000] * n
        prices[src] = 0
        for start, to, price in flights:
            graph[start].append((to, price))

        # Queue for BFS: (node, total price so far, stops made so far)
        q = deque([(src, 0, -1)])

        # BFS
        while q:
            node, price, stops = q.popleft()
            if stops+1 > k:
                continue
            
            for nei, p in graph[node]:
                if price + p < prices[nei]:
                    prices[nei] = price + p
                    q.append((nei, prices[nei], stops + 1))

        # Return the result if found, otherwise -1
        return prices[dst] if prices[dst] != 10000000 else -1

            