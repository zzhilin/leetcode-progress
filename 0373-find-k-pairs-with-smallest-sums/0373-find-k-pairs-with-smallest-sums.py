class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        pairs = []
        min_hp = []
        for i in range(min(k,len(nums1))):
            heapq.heappush(min_hp, (nums1[i]+nums2[0], i, 0))
        while min_hp and len(res) < k:
            _, i1, i2 = heappop(min_hp)
            res.append([nums1[i1], nums2[i2]])
            if i2+1 < len(nums2):
                heappush(min_hp, (nums1[i1] + nums2[i2+1], i1, i2+1))
        
        return res

