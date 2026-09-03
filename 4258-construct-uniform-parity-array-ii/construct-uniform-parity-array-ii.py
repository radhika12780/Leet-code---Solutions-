class Solution:
    def uniformArray(self, nums1):
        # Always possible to make all elements odd:
        # If there is at least one odd number, we can subtract the minimum odd number
        # from any even number to turn it odd (even - odd = odd).
        # Since nums1 consists of positive integers, if the minimum element is odd,
        # it is smaller than every even element, making nums1[i] - min_odd >= 1.
        
        # Always possible to make all elements even:
        # If all numbers are already even, or if we can subtract an even number.
        # But specifically, if there are NO odd numbers, everything is already even (returns True).
        # If the minimum number overall is even, we cannot make all numbers odd because 
        # there is no odd number strictly smaller than the minimum even number.

        min_val = min(nums1)
        
        # If the smallest number in the array is odd, we can always transform 
        # all even numbers into odd numbers by subtracting this minimum odd value.
        if min_val % 2 != 0:
            return True
            
        # If the minimum number is even, check if the array already contains ONLY even numbers.
        for x in nums1:
            if x % 2 != 0:
                return False
                
        return True