class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # check if it's valid palindrome
        def is_valid(substr):
            i = 0
            j = len(substr)-1
            while i < j:
                if substr[i] != substr[j]:
                    return False
                i += 1
                j -= 1
            return True
                
        
        # find possible partitions
        def find_partitions(index, curr):
            '''
            takes start index and curr list of partitions
            '''
            # reach end of s, add curr list to results
            if index == len(s):
                res.append(curr[:])
                return
            if index > len(s):
                return
            # for character in s
            for i in range(index, len(s)):
                substring = s[index:i+1]
                if not is_valid(substring):
                    continue
                curr.append(substring)
                find_partitions(i+1, curr)
                curr.pop()
        
        res = []
        curr = []
        find_partitions(0,curr)
        return res