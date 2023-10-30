class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_hp = []
        res = []
        for p in points:
            dist = math.dist(p, [0,0])
            min_hp.append((dist, p))
        heapq.heapify(min_hp)
        while k:
            res.append(heapq.heappop(min_hp)[1])
            k-=1
        return res