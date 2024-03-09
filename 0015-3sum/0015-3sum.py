class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # to use oppo ptrs
        # opposite direction
        res = []
        n = len(nums)
        # keep i, find nums[j]+nums[k] = -nums[i]
        for i in range(n-2):
            # if we encounter same number in nums (we cannot have dup triplets)
            # continue
            # not first num and curr equal to last number
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1

                elif s < 0:
                    j += 1
                else:
                    r = [nums[i], nums[j], nums[k]]
                    res.append(r)
                    # remove dup j and k
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res
	
