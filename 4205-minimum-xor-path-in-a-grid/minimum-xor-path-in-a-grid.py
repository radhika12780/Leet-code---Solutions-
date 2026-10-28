class Solution:
    def minCost(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # Har column ke liye reachable XOR values ka set
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        # First row (sirf right move kar sakte hain)
        for j in range(1, n):
            val = grid[0][j]
            for x in dp[j - 1]:
                dp[j].add(x ^ val)
        
        # Baaki rows process karo
        for i in range(1, m):
            # First column (sirf down move)
            new_dp0 = set()
            val = grid[i][0]
            for x in dp[0]:
                new_dp0.add(x ^ val)
            dp[0] = new_dp0
            
            # Middle columns (up or left se)
            for j in range(1, n):
                new_set = set()
                val = grid[i][j]
                
                # Upar se
                for x in dp[j]:
                    new_set.add(x ^ val)
                
                # Left se
                for x in dp[j - 1]:
                    new_set.add(x ^ val)
                
                dp[j] = new_set
        
        # Bottom-right cell me minimum XOR value return karo
        return min(dp[-1])