class Solution:
    def maxSumOfSquares(self, num, sum):
        # Return empty string if sum is impossible for num digits
        if sum > 9 * num:
            return ""

        # Find how many 9s fit in the sum
        nines = sum // 9
        rem = sum % 9

        # If sum divides evenly by 9
        if rem == 0:
            zeros = num - nines
            return "9" * nines + "0" * zeros

        # Fill with nines, the middle remainder digit, and zeros
        zeros = num - nines - 1
        return "9" * nines + str(rem) + "0" * zeros