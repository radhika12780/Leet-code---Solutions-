from collections import defaultdict

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            num = nums[right]
            freq[num] += 1
            
            # Shrink window if frequency of current number exceeds k
            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
            
            # Update maximum length found so far
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len