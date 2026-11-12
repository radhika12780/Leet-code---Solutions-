class Solution:
    def longestMonotonicSubarray(self, nums):
        # Every single element by itself is a valid subarray of length 1
        max_len = 1
        inc_len = 1
        dec_len = 1
        
        for i in range(1, len(nums)):
            # Check if strictly increasing
            if nums[i] > nums[i - 1]:
                inc_len += 1
                dec_len = 1
            # Check if strictly decreasing
            elif nums[i] < nums[i - 1]:
                dec_len += 1
                inc_len = 1
            # Reset both if numbers are equal
            else:
                inc_len = 1
                dec_len = 1
                
            # Update the longest length found so far
            max_len = max(max_len, inc_len, dec_len)
            
        return max_len