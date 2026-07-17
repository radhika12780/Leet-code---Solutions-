import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)
        
        # Step 1: Count frequencies of each number
        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1
            
        # Step 2 & 3: Compute exact pair counts for each GCD using inclusion-exclusion
        gcd_counts = [0] * (max_val + 1)
        
        for i in range(max_val, 0, -1):
            # Count how many elements in nums are multiples of i
            total_multiples = 0
            for j in range(i, max_val + 1, i):
                total_multiples += counts[j]
                
            # Total pairs that have a GCD equal to i or a multiple of i
            pairs = (total_multiples * (total_multiples - 1)) // 2
            
            # Subtract pairs that have a strictly larger multiple of i as their GCD
            for j in range(2 * i, max_val + 1, i):
                pairs -= gcd_counts[j]
                
            gcd_counts[i] = pairs
            
        # Step 4: Build prefix sums of the GCD pair counts
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_counts[i]
            
        # Step 5: Answer each query using binary search
        ans = []
        for q in queries:
            # We look for the first index where prefix_sums[idx] > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans