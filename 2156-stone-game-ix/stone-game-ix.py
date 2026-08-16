class Solution:
    def stoneGameIX(self, stones):
        # Count the frequency of remainders (0, 1, and 2)
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1
            
        c0 = count[0]
        c1 = count[1]
        c2 = count[2]
        
        # If count of 0s is even: Alice wins if both 1s and 2s exist
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        
        # If count of 0s is odd: Alice wins if the difference between 1s and 2s is >= 3
        return abs(c1 - c2) > 2