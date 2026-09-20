class Solution:
    def reverseDegree(self, s):
        total = 0
        
        for index, char in enumerate(s, 1):
            # 'a' is 26, 'b' is 25, ..., 'z' is 1
            alphabet_val = 26 - (ord(char) - ord('a'))
            total += alphabet_val * index
            
        return total