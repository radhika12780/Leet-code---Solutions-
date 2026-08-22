class Solution(object):

    def checkDivisibility(self, n):
        digits = [int(digit) for digit in str(n)]

        digit_sum = sum(digits)

        digit_product = 1
        for digit in digits:
            digit_product *= digit

        total_value = digit_sum + digit_product

        return n % total_value == 0