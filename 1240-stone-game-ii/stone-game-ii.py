class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        
        # Calculate suffix sums so we can get sum of remaining piles in O(1)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def play(i, m):
            # If we reached the end of piles
            if i >= n:
                return 0
            
            # If player can take all remaining piles in one move
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            # Check memoization table
            if (i, m) in memo:
                return memo[(i, m)]
            
            max_stones = 0
            # Try taking X piles where 1 <= X <= 2*M
            for x in range(1, 2 * m + 1):
                # Total remaining stones - best score the opponent can get
                next_m = max(m, x)
                stones = suffix_sum[i] - play(i + x, next_m)
                max_stones = max(max_stones, stones)
                
            memo[(i, m)] = max_stones
            return max_stones
        
        return play(0, 1)