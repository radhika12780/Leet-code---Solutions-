class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        
        # If target is longer than source, impossible to match
        if n > m:
            return 0
        
        # dp[j] stores ways to match t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string match

        # Iterate through s, updating dp backwards to avoid overwriting state
        for char in s:
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]