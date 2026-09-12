from bisect import bisect_right

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        
        # Store: [start, end, weight, original_index]
        arr = []
        for i in range(n):
            arr.append([intervals[i][0], intervals[i][1], intervals[i][2], i])
        
        # Sort intervals by end time for standard interval DP
        arr.sort(key=lambda x: x[1])
        
        ends = [x[1] for x in arr]
        
        # dp[i][k] = (max_weight, sorted_list_of_indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            curr_start, curr_end, weight, orig_idx = arr[i - 1]
            
            # Binary search: find largest index j where ends[j] < curr_start
            p = bisect_right(ends, curr_start - 1)
            
            for k in range(1, 5):
                # Option 1: Don't pick current interval
                best_w, best_idx = dp[i - 1][k]
                
                # Option 2: Pick current interval
                prev_w, prev_idx = dp[p][k - 1]
                pick_w = prev_w + weight
                
                # Keep indices sorted to guarantee correct lexicographical comparison
                pick_idx = sorted(prev_idx + [orig_idx])
                
                # Lexicographical tie-breaking
                if pick_w > best_w:
                    best_w = pick_w
                    best_idx = pick_idx
                elif pick_w == best_w and pick_w > 0:
                    if not best_idx or pick_idx < best_idx:
                        best_w = pick_w
                        best_idx = pick_idx
                
                dp[i][k] = (best_w, best_idx)
        
        # Find maximum weight across choosing 1, 2, 3, or 4 intervals
        res_w = 0
        res_idx = []
        for k in range(1, 5):
            w, idx = dp[n][k]
            if w > res_w:
                res_w = w
                res_idx = idx
            elif w == res_w and w > 0:
                if not res_idx or idx < res_idx:
                    res_idx = idx
                    
        return res_idx