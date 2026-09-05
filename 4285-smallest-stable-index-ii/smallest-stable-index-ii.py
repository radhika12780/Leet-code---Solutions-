class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # Suffix minimum array (Right to Left)
        suff_min = [0] * n
        suff_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] < suff_min[i + 1]:
                suff_min[i] = nums[i]
            else:
                suff_min[i] = suff_min[i + 1]

        # Running max & instability score check (Left to Right)
        curr_max = nums[0]

        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]

            instability_score = curr_max - suff_min[i]

            if instability_score <= k:
                return i

        return -1