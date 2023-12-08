class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # empty str is one group
        # same char count -> anagrams
        
        res = []
        anagrams = {}
        # each word converts to hashmap of word freq
        for word in strs:
            freqs = [0]*26
            for c in word:
                idx = ord(c) - ord('a')
                freqs[idx] += 1
            # only tuple is hashable and can be key
            k = tuple(freqs)
            # freqs is the key to find anagrams 
            if k not in anagrams:
                anagrams[k] = []
            anagrams[k].append(word)
        return anagrams.values()