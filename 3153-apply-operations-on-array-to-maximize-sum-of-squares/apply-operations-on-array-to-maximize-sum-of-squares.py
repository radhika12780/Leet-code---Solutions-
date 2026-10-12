class Solution:
    def maxSum(self, nums, k):
        MOD = 1000000007

        # Count how many times each bit is set to 1 across all numbers
        bit_counts = [0] * 30
        for num in nums:
            for i in range(30):
                if (num >> i) & 1:
                    bit_counts[i] += 1

        total_sum = 0

        # Build the k largest possible numbers greedily
        for _ in range(k):
            current_num = 0
            for i in range(30):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1

            total_sum = (total_sum + current_num * current_num) % MOD

        return total_sum