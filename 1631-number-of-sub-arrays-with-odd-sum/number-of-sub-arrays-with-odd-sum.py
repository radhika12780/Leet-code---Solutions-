class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        
        # Start with even_count = 1 to represent an empty prefix sum of 0
        even_count = 1
        odd_count = 0
        
        prefix_sum = 0
        total_subarrays = 0
        
        for num in arr:
            prefix_sum += num
            
            # If the running sum is odd, pair it with any previous even prefix sum
            if prefix_sum % 2 == 1:
                total_subarrays = (total_subarrays + even_count) % MOD
                odd_count += 1
            # If the running sum is even, pair it with any previous odd prefix sum
            else:
                total_subarrays = (total_subarrays + odd_count) % MOD
                even_count += 1
                
        return total_subarrays