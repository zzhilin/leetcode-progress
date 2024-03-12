class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        total = 0
        min_diff = float("inf")
        
        for i in range(n-2):
            # op 3
            if i and nums[i-1] == nums[i]:
                continue
                
            #op 1
            s = nums[i] + nums[i+1] + nums[i+2]
            if s > target:
                diff = abs(s - target)
                if diff < min_diff:
                    total = s
                break
                
            # op 2
            s = nums[i] + nums[n-1] + nums[n-2]
            if s < target:
                diff = abs(target - s)
                if diff < min_diff:
                    min_diff = diff
                    total = s
                continue
                
            j, k = i + 1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s < target:
                    diff = target-s
                    if diff < min_diff:
                        min_diff = diff
                        total = s
                    j += 1
                else:
                    diff = s - target
                    if diff < min_diff:
                        min_diff = diff
                        total = s
                    
                    k -= 1
        return total