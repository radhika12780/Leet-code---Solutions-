class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        
        # Precompute suffix minimums from right to left
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        current_max = nums[0]
        
        # Find the first index that meets the stability condition
        for i in range(n):
            current_max = max(current_max, nums[i])
            instability_score = current_max - suffix_min[i]
            
            if instability_score <= k:
                return i
                
        return -1