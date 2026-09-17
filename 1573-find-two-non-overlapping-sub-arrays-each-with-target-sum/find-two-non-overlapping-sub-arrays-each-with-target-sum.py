class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        
        # min_len[i] stores the smallest length of a subarray sum equal to target found in arr[0...i]
        min_len = [float('inf')] * n
        
        left = 0
        current_sum = 0
        best_single_len = float('inf')
        ans = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink window if sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            # Found a valid subarray
            if current_sum == target:
                curr_len = right - left + 1
                
                # Check if we already found a non-overlapping valid subarray before 'left'
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                
                best_single_len = min(best_single_len, curr_len)
            
            # Record the shortest subarray sum to target seen so far up to index 'right'
            min_len[right] = best_single_len
        
        return ans if ans != float('inf') else -1