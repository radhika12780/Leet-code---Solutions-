class Solution:
    def maxAlternatingSum(self, nums):
        # Step 1: Calculate the squares of all numbers
        squares = [x * x for x in nums]
        
        # Step 2: Sort all squared values
        squares.sort()
        
        n = len(squares)
        half = n // 2
        
        # Step 3: Subtract the smaller half and add the larger half
        return sum(squares[half:]) - sum(squares[:half])