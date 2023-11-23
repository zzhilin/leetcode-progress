class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(nums, num):
            n = len(nums)
            l, r = 0, n
            while l < r:
                mid = (l+r) // 2
                if nums[mid] < num:
                    l = mid+1
                else:
                    r = mid
            return l
        
        
        # build subsequence
        sub = []
        # if curr num is greater than prev num, add to sub
        for i in range(len(nums)):
            # print(sub)
            if len(sub) == 0 or nums[i] > sub[-1]:
                sub.append(nums[i])
        # if curr num is less than prev num, find smallest num in sub that >= curr num, replace
            else:
                pos = binary_search(sub, nums[i])
                sub[pos] = nums[i]
                
        # LIS is len(sub)
        return len(sub)
            