class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # "abbzzca" "babzzcz"
        # false - diff length, containing diff set of chars
        if len(word1) != len(word2):
            return False
        s1,s2 = set(word1), set(word2)
        if s1 != s2:
            return False
        c1, c2 = Counter(word1), Counter(word2)

        '''
        word1 a:2 b:2 c:1 z:2
        word2 a:1 b:2 c:1 z:3
        '''
        
        v1, v2 = sorted(c1.values()), sorted(c2.values())
        return v1==v2