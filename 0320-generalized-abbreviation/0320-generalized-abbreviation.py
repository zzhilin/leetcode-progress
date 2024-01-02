class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        '''
        w | 1
        o | 1 | o | 1
        r | 1 | r | 1 | r | 1 | r | 1
        '''
        res = []
        n = len(word)
        def backtrack(start, curr, cnt):
            if start == n:
                res.append(curr + str(cnt) if cnt > 0 else curr)
            else:
                # don't keep curr letter
                backtrack(start+1,curr,cnt+1)
                # keep curr letter
                backtrack(start+1, curr + (str(cnt) if cnt > 0 else '') + word[start], 0)
                
        
        backtrack(0, '', 0)
        return res