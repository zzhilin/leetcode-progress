class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        未知量：which player wins -> reduce colors so we cannot remove another A or B
已知数据：string colors contains only 'A' and B of length n
条件：start with alice, remove A, minimal AAA; bob removes B minimal BBB
重新阐述：in string of Aand/orB, remove ABAB alternate and returns when we cannot remove anymore (no A/B, all removable pieces are on edge)
例子：colors = 'AB', 返回结果为 F
        """
        # if either a or b are less than 3, 'abb' returns false because alice can't do anything
        # count = Counter(colors)
        # if count['A'] < 3:
        #     return False
        # if len(set(colors)) == len(colors):
        #     return False
        
        def find_valid_ranges_length(s, letter):
            valid_ranges_length = []
            current_char = letter
            current_length = 0
            
            for c in s:
                if c == current_char:
                    current_length += 1
                else:
                    if current_length >= 3:
                        valid_ranges_length.append(current_length)
                    current_length = 0
            
            if current_length >= 3:
                valid_ranges_length.append(current_length)
            return valid_ranges_length
        
        
        alice = find_valid_ranges_length(colors, 'A')
        bob = find_valid_ranges_length(colors, 'B')

        turns_a = [i-2 for i in alice]
        turns_b = [i-2 for i in bob]
        # print(turns_a,turns_b)
        if sum(turns_a) <= sum(turns_b):
            return False
        return True

        