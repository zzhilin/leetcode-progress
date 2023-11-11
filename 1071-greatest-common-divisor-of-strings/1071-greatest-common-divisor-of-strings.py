class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        str1: "ABABDD", str2: "ABAB"
        """
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            if str1 == str2:
                return str1
            return ''
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        splitted_s1 = str1.split(str2)
        empty = True
        leftover = ''
        for s in splitted_s1:
            if s != '':
                empty = False
                leftover = s
        if empty:
            return str2
        if leftover not in str2:
            return ''
        first = str2


        while leftover:
            first,leftover = leftover, first[:len(first)%len(leftover)]

        return first
