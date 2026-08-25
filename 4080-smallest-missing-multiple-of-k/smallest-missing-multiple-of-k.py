class Solution:
    def missingMultiple(self, nums, k):
        num_set = set(nums)
        multiple = k
        
        while multiple in num_set:
            multiple += k
            
        return multiple