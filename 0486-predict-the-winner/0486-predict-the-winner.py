class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def predict(l, r):
            if l == r:
                return nums[l]
            if l > r:
                return 0
            p1 = nums[l]+min(predict(l+2,r), predict(l+1,r-1))
            p2 = nums[r]+min(predict(l,r-2), predict(l+1,r-1))
            return max(p1,p2)
        
        curr = predict(0,len(nums)-1)
        return curr >= sum(nums)-curr