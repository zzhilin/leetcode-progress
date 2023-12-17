class Solution:
    def largestPalindromic(self, num: str) -> str:
        """
        {4:4,9:1,7:2,1:1,3:1}
        last/first has to be digit >= 2 occurrences
        we pick 7 b/c > 4 -> 7,,,,7
        pick 4 b/c other numbers cannot be palindrome 744...447
        
        """
        if all(x == '0' for x in num):
            return '0'
        freq = Counter(num)
        p = ''
        left,right = '',''
        middle = None
        nums = sorted(freq.items(), reverse=True)
        print(nums)

        for num, cnt in nums:
            if cnt % 2 == 0:
                if not left and not right and num == '0':
                    continue
                left += num * (cnt // 2)
                right += num * (cnt // 2)
            else:
                if not left and not right and num == '0':
                    continue
                if cnt % 2 != 0 and cnt > 1:
                    left += num * ((cnt-1)//2)
                    right += num * ((cnt-1)//2)
                if not middle:
                    middle = num
        if middle:
            p = left + middle + right[::-1]
        else:
            p = left + right[::-1]
        return p