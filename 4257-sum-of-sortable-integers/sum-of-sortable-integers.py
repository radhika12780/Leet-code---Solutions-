class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            ok = True
            prev_max = 0

            for i in range(0, n, k):
                block = nums[i:i + k]

                descents = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        descents += 1

                if descents > 1 or min(block) < prev_max:
                    ok = False
                    break

                prev_max = max(block)

            if ok:
                ans += k

        return ans