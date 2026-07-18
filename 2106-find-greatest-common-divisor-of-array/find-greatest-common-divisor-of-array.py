class Solution(object):
    def findGCD(self, nums):
        min_num = min(nums)
        max_num = max(nums)
        
        # Manual Euclidean algorithm compatible with Python 2
        while min_num:
            max_num, min_num = min_num, max_num % min_num
            
        return max_num