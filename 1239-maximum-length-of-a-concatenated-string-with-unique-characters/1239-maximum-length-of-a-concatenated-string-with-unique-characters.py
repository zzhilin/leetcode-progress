class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # backtracking?
        """
        未知量：str arr 中最长的可组合出的str，没有重复character
        已知数据：长度范围为 1 到 16，arr 有重复元素
        条件：合格的subsequence为没有重复
        重新阐述：一个只有小写字母的arr中找出可组合的最长unique s
        
        #how to handle duplicate items like "aa"
        """

        res = 0
        def dfs(start_i, combination):
            nonlocal res
            res = max(res, len(combination))

            for i in range(start_i,len(arr)):
                # has duplicate character
                next_s = arr[i]
                if len(next_s) != len(set(next_s)):
                    continue
                if not any(c in combination for c in next_s):
                    dfs(i+1,combination + arr[i])

        dfs(0,'')
        return res