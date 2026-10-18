import math

class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7

        # Simple combination function: nCr = n! / (r! * (n - r)!)
        def combinations(n, r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = []
            right = []

            for x in arr[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)

            left_ways = solve(left)
            right_ways = solve(right)

            # Count ways to interleave elements from both subtrees
            ways = combinations(len(left) + len(right), len(left))

            return (ways * left_ways * right_ways) % MOD

        return (solve(nums) - 1) % MOD