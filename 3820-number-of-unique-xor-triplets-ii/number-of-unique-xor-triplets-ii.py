class Solution:
    def uniqueXorTriplets(self, nums):
        # Clean helper function without 'self' or type annotations
        def solve(arr):
            # 1. Remove duplicates
            vals = list(set(arr))
            
            # 2. Find all unique XOR outcomes for 2 numbers
            pairs = set()
            for x in vals:
                for y in vals:
                    pairs.add(x ^ y)
            
            # 3. Combine pair XORs with a 3rd number
            triplets = set()
            for p in pairs:
                for z in vals:
                    triplets.add(p ^ z)
            
            return len(triplets)

        return solve(nums)