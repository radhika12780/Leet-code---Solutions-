class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        if n <= 2:
            return n

        # Find the 0-indexed positions of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Order indices so i is always the left-most index
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)

        # 3 Options:
        # 1) Delete both from front: j + 1
        # 2) Delete both from back: n - i
        # 3) Delete from both sides: (i + 1) + (n - j)
        return min(j + 1, n - i, (i + 1) + (n - j))