class Solution:
    def stoneGameVIII(self, stones):
        # Build prefix sums array
        total_sum = 0
        prefix_sums = []
        for stone in stones:
            total_sum += stone
            prefix_sums.append(total_sum)

        # Work backwards to find maximum score difference
        best_diff = prefix_sums[-1]
        
        for i in range(len(stones) - 2, 0, -1):
            best_diff = max(best_diff, prefix_sums[i] - best_diff)

        return best_diff