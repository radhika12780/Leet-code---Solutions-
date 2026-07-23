class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Base cases for small arrays
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # For n >= 3, we can form all values up to (2 ** bit_length) - 1
        return 1 << n.bit_length()