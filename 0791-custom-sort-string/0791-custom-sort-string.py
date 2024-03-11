class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1
            
        sorted_s = ''
        for char in order:
            sorted_s += char * char_count[char]
            
        for char in s:
            if char not in order:
                sorted_s += char
        return sorted_s