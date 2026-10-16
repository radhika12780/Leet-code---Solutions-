class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.sum_val = [0] * (4 * size)
        self.sum_sq = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push_down(self, node, left, right):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (left + right) // 2
            
            # Update left child
            len_l = mid - left + 1
            self.sum_sq[2 * node] += 2 * val * self.sum_val[2 * node] + val * val * len_l
            self.sum_val[2 * node] += val * len_l
            self.lazy[2 * node] += val

            # Update right child
            len_r = right - mid
            self.sum_sq[2 * node + 1] += 2 * val * self.sum_val[2 * node + 1] + val * val * len_r
            self.sum_val[2 * node + 1] += val * len_r
            self.lazy[2 * node + 1] += val

            self.lazy[node] = 0

    def update(self, node, left, right, ql, qr, val):
        if ql <= left and right <= qr:
            length = right - left + 1
            self.sum_sq[node] += 2 * val * self.sum_val[node] + val * val * length
            self.sum_val[node] += val * length
            self.lazy[node] += val
            return

        self._push_down(node, left, right)
        mid = (left + right) // 2
        if ql <= mid:
            self.update(2 * node, left, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, right, ql, qr, val)

        self.sum_val[node] = self.sum_val[2 * node] + self.sum_val[2 * node + 1]
        self.sum_sq[node] = self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]


class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        tree = SegmentTree(n)
        
        last_pos = {}
        total_sum = 0

        for i, val in enumerate(nums):
            prev = last_pos.get(val, -1)
            
            # Increment distinct counts for starting positions from (prev + 1) to i
            tree.update(1, 0, n - 1, prev + 1, i, 1)
            
            # Accumulate sum of squares modulo 10^9 + 7
            total_sum = (total_sum + tree.sum_sq[1]) % MOD
            
            # Store current index for value
            last_pos[val] = i

        return total_sum