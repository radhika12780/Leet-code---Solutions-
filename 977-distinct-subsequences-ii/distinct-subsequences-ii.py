class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        ends_with = [0] * 26

        for char in s:
            char_idx = ord(char) - ord("a")
            # The new subsequences ending with 'char' equal 
            # 1 (for 'char' itself) + total of all subsequences formed so far
            ends_with[char_idx] = (sum(ends_with) + 1) % MOD

        return sum(ends_with) % MOD