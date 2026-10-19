class Solution:
    def targetIndices(self, nums, target):
        less_count = 0
        target_count = 0

        for num in nums:
            if num < target:
                less_count += 1
            elif num == target:
                target_count += 1

        result = []
        for i in range(target_count):
            result.append(less_count + i)

        return result