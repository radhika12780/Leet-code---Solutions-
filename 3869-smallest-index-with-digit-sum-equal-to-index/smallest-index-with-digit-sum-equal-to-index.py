class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            # Calculate sum of digits for nums[i]
            total = 0
            val = nums[i]
            while val > 0:
                total += val % 10
                val //= 10
            
            # Check if digit sum equals index
            if total == i:
                return i
                
        return -1
        