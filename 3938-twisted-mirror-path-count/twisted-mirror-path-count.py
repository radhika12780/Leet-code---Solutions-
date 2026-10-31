class Solution:
    def uniquePaths(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        memo = {}

        def get_landing(r, c, d):
            if r >= m or c >= n:
                return None
            if grid[r][c] == 0:
                return (r, c)

            state = (r, c, d)
            if state in memo:
                return memo[state]

            # d = 0 means entered moving Right -> reflect Down (r + 1, c)
            # d = 1 means entered moving Down  -> reflect Right (r, c + 1)
            if d == 0:
                res = get_landing(r + 1, c, 1)
            else:
                res = get_landing(r, c + 1, 0)

            memo[state] = res
            return res

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0 or grid[r][c] == 1:
                    continue

                # Try moving Right into (r, c + 1)
                land_r = get_landing(r, c + 1, 0)
                if land_r:
                    lr, lc = land_r
                    dp[lr][lc] = (dp[lr][lc] + dp[r][c]) % MOD

                # Try moving Down into (r + 1, c)
                land_d = get_landing(r + 1, c, 1)
                if land_d:
                    dr, dc = land_d
                    dp[dr][dc] = (dp[dr][dc] + dp[r][c]) % MOD

        return dp[m - 1][n - 1]