class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while st and curr > temperatures[st[-1]]:
                prev = st.pop()
                res[prev] = i-prev
            st.append(i)
        return res
            
        