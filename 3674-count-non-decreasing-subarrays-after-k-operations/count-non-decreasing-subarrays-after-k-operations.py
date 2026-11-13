from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        # Deque stores [value, count_of_elements_merged_into_this_value]
        blocks = deque()
        
        total_valid = 0
        current_cost = 0
        right = n - 1
        
        # Slide the left pointer backwards from n-1 down to 0
        for left in range(n - 1, -1, -1):
            val = nums[left]
            count = 1
            
            # Merge any right-hand blocks that are smaller than the current element
            while blocks and blocks[0][0] < val:
                block_val, block_count = blocks.popleft()
                current_cost += (val - block_val) * block_count
                count += block_count
                
            blocks.appendleft([val, count])
            
            # Shrink the window from the right if total operations exceed k
            while current_cost > k:
                right_val, right_count = blocks[-1]
                # Removing one element from the rightmost block reduces cost by (right_val - nums[right])
                current_cost -= (right_val - nums[right])
                right -= 1
                
                if right_count == 1:
                    blocks.pop()
                else:
                    blocks[-1][1] -= 1
                    
            # Every subarray starting at 'left' and ending anywhere up to 'right' is valid
            total_valid += (right - left + 1)
            
        return total_valid