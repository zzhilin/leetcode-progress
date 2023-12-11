class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        pushed = deque(pushed)
        popped = deque(popped)
        while pushed and popped:
            to_add = pushed.popleft()
            st.append(to_add)
            while st and st[-1] == popped[0]:
                st.pop()
                popped.popleft()
        return len(st) == 0
                
            