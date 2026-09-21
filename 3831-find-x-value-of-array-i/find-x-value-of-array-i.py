class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            rem = num % k
            new_dp = [0] * k
            
            # Start a new subarray at current element
            new_dp[rem] += 1

            # Extend previous subarrays with current element
            for prev_rem in range(k):
                if dp[prev_rem] > 0:
                    nxt = (prev_rem * rem) % k
                    new_dp[nxt] += dp[prev_rem]

            # Accumulate counts into the final answer array
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans