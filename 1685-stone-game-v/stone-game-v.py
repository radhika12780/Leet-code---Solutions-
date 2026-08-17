class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        
        # Calculate prefix sums for quick range sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        
        # Auxiliary tables to keep track of optimal choices in O(1) time
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]

        # Base cases for single stones
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        # Fill DP table by increasing subarray length
        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Find the boundary where left sum >= right sum
                total_sum = prefix[j + 1] - prefix[i]
                while (prefix[mid + 1] - prefix[i]) * 2 < total_sum:
                    mid += 1

                left_sum = prefix[mid + 1] - prefix[i]
                
                # Case 1: left sum and right sum are equal
                if left_sum * 2 == total_sum:
                    dp[i][j] = max(max_left[i][mid], max_right[mid + 1][j])
                else:
                    # Case 2: left sum is smaller or right sum is smaller
                    left_part = max_left[i][mid - 1] if mid > i else 0
                    right_part = max_right[mid + 1][j] if mid < j else 0
                    dp[i][j] = max(left_part, right_part)

                # Maintain auxiliary max values for future O(1) lookups
                max_left[i][j] = max(max_left[i][j - 1], dp[i][j] + total_sum)
                max_right[i][j] = max(max_right[i + 1][j], dp[i][j] + total_sum)

        return dp[0][n - 1]