class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        
        # Calculate initial absolute differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        # Frequency bucket array for differences
        max_diff = max(diffs)
        if max_diff == 0 or k == 0:
            return sum(d * d for d in diffs)
        
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
        
        # Reduce differences greedily from largest to smallest
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
            
            # How many reductions can we perform at this level?
            take = min(k, count[d])
            count[d] -= take
            count[d - 1] += take
            k -= take
            
            if k == 0:
                break
        
        # Calculate sum of squared differences
        return sum(c * (d ** 2) for d, c in enumerate(count))
        