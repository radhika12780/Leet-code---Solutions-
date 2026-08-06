class Solution:
    def smallestNumber(self, n, t):
        while True:
            # Calculate the product of digits of n
            digit_product = 1
            for digit in str(n):
                digit_product *= int(digit)
            
            # Check if the digit product is divisible by t
            if digit_product % t == 0:
                return n
            
            # Move to the next number
            n += 1