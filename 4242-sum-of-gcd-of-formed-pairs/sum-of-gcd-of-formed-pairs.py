from fractions import gcd

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefixGcd = [0] * n
        
        # Step 1: Compute prefixGcd while maintaining the running maximum
        current_max = 0
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            prefixGcd[i] = gcd(nums[i], current_max)
            
        # Step 2: Sort the array in non-decreasing order
        prefixGcd.sort()
        
        # Step 3: Pair using two pointers (smallest with largest)
        total_sum = 0
        left, right = 0, n - 1
        
        while left < right:
            total_sum += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum