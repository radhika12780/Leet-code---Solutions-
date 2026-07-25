class Solution:
    def maxProduct(self, n):
        # Convert n to a list of integer digits and sort them
        digits = sorted(int(d) for d in str(n))
        
        # Multiply the two largest digits at the end of the list
        return digits[-1] * digits[-2]