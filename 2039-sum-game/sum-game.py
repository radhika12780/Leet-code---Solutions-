class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2
        
        left_sum = 0
        left_q = 0
        right_sum = 0
        right_q = 0
        
        # Calculate totals for the first half
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
                
        # Calculate totals for the second half
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
                
        # Alice wins if the total balance condition doesn't match Bob's winning ratio
        sum_diff = left_sum - right_sum
        q_diff = right_q - left_q
        
        return sum_diff * 2 != q_diff * 9