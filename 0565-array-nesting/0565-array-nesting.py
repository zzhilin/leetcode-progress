class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        res = float("-inf")
        
        # go over all numbers
        for i in range(len(nums)):
            # not visited
            if nums[i] != float("inf"):
                length = 0
                curr = nums[i]
                # no dup in set yet
                while nums[curr] != float("inf"):
                    val = curr
                    # update next index
                    curr = nums[curr]
                    # set current index to visited
                    nums[val] = float("inf")
                    # update count
                    length += 1
                res = max(res, length)
        return res