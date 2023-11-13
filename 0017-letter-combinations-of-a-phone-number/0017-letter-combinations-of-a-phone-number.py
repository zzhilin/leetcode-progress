class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        general time complexity: number of children of each node ^ height of the state tree.
        time: 4(max possible children)^N(digits len) * N
        n
        """
        if not digits:
            return []
        mapping = {'2': ['a','b','c'], '3':['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                  '5':['j','k','l'],'6':['m','n','o'], '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        def backtrack(start, path):
            # if we got same len as digits, we got the solution
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            # generate possible children
            for letter in mapping[digits[start]]:
                path.append(letter)
                backtrack(start+1, path)
                path.pop()
        res = []
        backtrack(0, [])
        return res
            