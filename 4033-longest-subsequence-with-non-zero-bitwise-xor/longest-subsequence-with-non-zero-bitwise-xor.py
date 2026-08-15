class Solution:
    def longestSubsequence(self, nums):
        # 1. If every number is 0, we can't make a non-zero XOR sum
        if max(nums) == 0:
            return 0
        
        # 2. Calculate the bitwise XOR of the full array
        total_xor = 0
        for x in nums:
            total_xor ^= x
            
        # 3. If total XOR is already non-zero, use the whole array
        if total_xor != 0:
            return len(nums)
        
        # 4. Otherwise, drop one non-zero element to make the XOR non-zero
        return len(nums) - 1