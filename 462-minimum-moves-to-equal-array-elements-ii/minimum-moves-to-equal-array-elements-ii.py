class Solution:
    def minMoves2(self, nums):
        # Sort the array to easily access the median
        nums.sort()
        
        # Pick the middle element (median) as our target number
        target = nums[len(nums) // 2]
        
        moves = 0
        # Sum the absolute differences between each element and the target
        for num in nums:
            moves += abs(num - target)
            
        return moves