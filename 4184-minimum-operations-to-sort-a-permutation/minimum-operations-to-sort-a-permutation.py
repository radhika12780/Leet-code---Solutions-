class Solution:
    def minOperations(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        
        # Find index of element 0
        zero_pos = 0
        for i in range(n):
            if nums[i] == 0:
                zero_pos = i
                break

        # Check if cyclically increasing
        is_increasing = True
        for i in range(n - 1):
            if nums[(zero_pos + i + 1) % n] != nums[(zero_pos + i) % n] + 1:
                is_increasing = False
                break

        # Check if cyclically decreasing
        is_decreasing = True
        for i in range(n - 1):
            if nums[(zero_pos - (i + 1)) % n] != nums[(zero_pos - i) % n] + 1:
                is_decreasing = False
                break

        # If it matches neither pattern, it's impossible
        if not is_increasing and not is_decreasing:
            return -1

        ans = float('inf')

        # Calculate best cost if cyclically increasing
        if is_increasing:
            cost_rotate = zero_pos
            cost_reverse_combo = (n - zero_pos) + 2
            ans = min(ans, cost_rotate, cost_reverse_combo)

        # Calculate best cost if cyclically decreasing
        if is_decreasing:
            cost_rev_then_rot = n - zero_pos
            cost_rot_then_rev = zero_pos + 2
            ans = min(ans, cost_rev_then_rot, cost_rot_then_rev)

        return ans