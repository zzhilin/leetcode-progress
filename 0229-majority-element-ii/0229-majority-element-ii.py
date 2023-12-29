class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        candidate1, counter1 = None, 0
        candidate2, counter2 = None, 0
        for num in nums:
            if candidate1 == num:
                counter1 += 1
            elif candidate2 == num:
                counter2 += 1
            elif counter1 == 0:
                candidate1 = num
                counter1 += 1
            elif counter2 == 0:
                candidate2 = num
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1
                
        threshold = len(nums)//3
        res = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > threshold:
                res.append(c)
        return res
            