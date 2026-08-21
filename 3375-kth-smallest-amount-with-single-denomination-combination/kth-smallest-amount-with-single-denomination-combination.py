class Solution:
    def findKthSmallest(self, coins, k):
        def compute_lcm(a, b):
            x, y = a, b
            while y:
                x, y = y, x % y
            return (a * b) // x

        def count_valid_amounts(target_amount):
            total_count = 0
            n = len(coins)
            
            for mask in range(1, 1 << n):
                current_lcm = 1
                bits_set = 0
                
                for i in range(n):
                    if (mask >> i) & 1:
                        bits_set += 1
                        current_lcm = compute_lcm(current_lcm, coins[i])
                        if current_lcm > target_amount:
                            break
                            
                if current_lcm <= target_amount:
                    if bits_set % 2 == 1:
                        total_count += target_amount // current_lcm
                    else:
                        total_count -= target_amount // current_lcm
                        
            return total_count

        low = 1
        high = min(coins) * k
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if count_valid_amounts(mid) >= k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer