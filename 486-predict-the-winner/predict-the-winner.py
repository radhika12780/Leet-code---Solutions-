class Solution:
    def predictTheWinner(self, nums):
        memo = {}

        def get_max_diff(i, j):
            if i == j:
                return nums[i]

            if (i, j) in memo:
                return memo[(i, j)]

            # The current player can either pick from the left or right end.
            # We subtract the opponent's maximum score difference in the remaining subarray.
            pick_left = nums[i] - get_max_diff(i + 1, j)
            pick_right = nums[j] - get_max_diff(i, j - 1)

            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        # If the maximum score difference for Player 1 is >= 0, Player 1 wins or ties.
        return get_max_diff(0, len(nums) - 1) >= 0