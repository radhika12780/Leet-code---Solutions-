class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        total_n = n + k - 1
        total_r = 2 * k
        
        # Calculate combination nCr = (n!) / (r! * (n-r)!) directly
        ans = 1
        for i in range(1, total_r + 1):
            ans = ans * (total_n - i + 1) // i
            
        return ans % MOD