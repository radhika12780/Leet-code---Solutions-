class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        
        for x in arr1:
            # Check if any element in arr2 is close to x (distance <= d)
            if not any(abs(x - y) <= d for y in arr2):
                count += 1
                
        return count