class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = {}
        best = 0
        
        for num in nums:
            dp[num + 1] = dp.get(num, 0) + 1
            dp[num] = dp.get(num - 1, 0) + 1
            
            if dp[num + 1] > best:
                best = dp[num + 1]
            if dp[num] > best:
                best = dp[num]
                
        return best