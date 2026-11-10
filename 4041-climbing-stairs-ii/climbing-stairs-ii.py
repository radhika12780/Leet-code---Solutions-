class Solution(object):
    def climbStairs(self, n, costs):
        # min_cost[i] will store the minimum cost to reach step i
        min_cost = [0] * (n + 1)
        
        for i in range(1, n + 1):
            best = float('inf')
            
            # Check all valid jumps coming into step i (1, 2, or 3 steps back)
            for k in range(1, 4):
                if i - k >= 0:
                    prev_step = i - k
                    # Jump cost formula: costs[i-1] + (k * k)
                    # Note: costs array is 1-indexed in problem description, so step i is costs[i-1]
                    jump_cost = min_cost[prev_step] + costs[i - 1] + (k * k)
                    if jump_cost < best:
                        best = jump_cost
                        
            min_cost[i] = best
            
        return min_cost[n]