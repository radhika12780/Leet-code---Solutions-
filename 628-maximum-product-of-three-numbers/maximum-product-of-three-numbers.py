class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        
        # Choice 1: The product of the 3 largest numbers
        option1 = nums[-1] * nums[-2] * nums[-3]
        
        # Choice 2: The product of the 2 smallest numbers (which could be negative) and the largest number
        option2 = nums[0] * nums[1] * nums[-1]
        
        # Return whichever choice gives the larger value
        return max(option1, option2)