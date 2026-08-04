class Solution(object):

    def findMissingElements(self, nums):
        seen = set(nums)
        start = min(nums)
        end = max(nums)

        missing = []
        for number in range(start, end + 1):
            if number not in seen:
                missing.append(number)

        return missing