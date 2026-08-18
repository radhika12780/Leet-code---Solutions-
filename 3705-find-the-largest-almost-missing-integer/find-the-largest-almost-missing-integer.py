class Solution:

    def largestInteger(self, nums, k):
        n = len(nums)
        subarray_counts = {}

        # Iterate over all possible subarrays of size k
        for i in range(n - k + 1):
            # Collect unique elements in the current subarray
            unique_in_subarray = set(nums[i : i + k])

            # Increment count for each unique element present in this subarray
            for num in unique_in_subarray:
                subarray_counts[num] = subarray_counts.get(num, 0) + 1

        # Find the maximum value that appears in exactly 1 subarray
        ans = -1
        for num, count in subarray_counts.items():
            if count == 1:
                if num > ans:
                    ans = num

        return ans