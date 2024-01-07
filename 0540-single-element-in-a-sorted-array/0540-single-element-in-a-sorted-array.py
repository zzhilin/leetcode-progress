class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # remove a pair -> left subarr and right subarr
        # the subarr with single element must be odd length
        '''
        由于给定数组有序 且 常规元素总是两两出现，因此如果不考虑“特殊”的单一元素的话，我们有结论：成对元素中的第一个所对应的下标必然是偶数，成对元素中的第二个所对应的下标必然是奇数。

然后再考虑存在单一元素的情况，假如单一元素所在的下标为 x，那么下标 x 之前（左边）的位置仍满足上述结论，而下标 x 之后（右边）的位置由于 x 的插入，导致结论翻转。

存在这样的二段性，指导我们根据当前二分点 midmidmid 的奇偶性进行分情况讨论：

midmidmid 为偶数下标：根据上述结论，正常情况下偶数下标的值会与下一值相同，因此如果满足该条件，可以确保 midmidmid 之前并没有插入单一元素。正常情况下，此时应该更新 l=midl = midl=mid，否则应当让 r=mid−1r = mid - 1r=mid−1，但需要注意这样的更新逻辑，会因为更新 rrr 时否决 midmidmid 而错过答案，我们可以将否决 midmidmid 的动作放到更新 lll 的一侧，即需要将更新逻辑修改为 l=mid+1l = mid + 1l=mid+1 和 r=midr = midr=mid ；

midmidmid 为奇数下标：同理，根据上述结论，正常情况下奇数下标的值会与上一值相同，因此如果满足该条件，可以确保 midmidmid 之前并没有插入单一元素，相应的更新 lll 和 rrr。

        '''
        
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 0:
                if mid + 1 < hi+1 and nums[mid] == nums[mid+1]:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                if mid - 1 >= 0 and nums[mid] == nums[mid-1]:
                    lo = mid + 1
                else:
                    hi = mid
        return nums[lo]
            