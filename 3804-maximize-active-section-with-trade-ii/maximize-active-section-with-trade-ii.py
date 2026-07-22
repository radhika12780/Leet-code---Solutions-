from bisect import bisect_left, bisect_right


class Solution:

    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        total_ones = s.count("1")

        # 1. Compress into zero blocks: (start_idx, end_idx, length)
        zero_blocks = []
        i = 0
        while i < n:
            if s[i] == "0":
                start = i
                while i < n and s[i] == "0":
                    i += 1
                zero_blocks.append((start, i - 1, i - start))
            else:
                i += 1

        num_zero_blocks = len(zero_blocks)
        if num_zero_blocks < 2:
            return [total_ones] * len(queries)

        # 2. Adjacent zero-block gains
        adjacent_gains = [
            zero_blocks[k][2] + zero_blocks[k + 1][2]
            for k in range(num_zero_blocks - 1)
        ]
        num_gains = len(adjacent_gains)

        # 3. Build Segment Tree for fast Range Maximum Queries (RMQ)
        tree_size = 1
        while tree_size < num_gains:
            tree_size *= 2
        tree = [0] * (2 * tree_size)

        for k in range(num_gains):
            tree[tree_size + k] = adjacent_gains[k]
        for k in range(tree_size - 1, 0, -1):
            tree[k] = max(tree[2 * k], tree[2 * k + 1])

        def query_max(l, r):
            if l > r:
                return 0
            l += tree_size
            r += tree_size
            ans = 0
            while l <= r:
                if l % 2 == 1:
                    ans = max(ans, tree[l])
                    l += 1
                if r % 2 == 0:
                    ans = max(ans, tree[r])
                    r -= 1
                l //= 2
                r //= 2
            return ans

        # 4. Binary search start positions
        starts = [b[0] for b in zero_blocks]

        # 5. Process queries in O(log N) time each
        res = []
        for ql, qr in queries:
            first_idx = bisect_left(starts, ql)
            last_idx = bisect_right(starts, qr) - 1

            if (
                first_idx > 0
                and zero_blocks[first_idx - 1][0]
                <= ql
                <= zero_blocks[first_idx - 1][1]
            ):
                first_idx -= 1

            if first_idx >= last_idx:
                res.append(total_ones)
                continue

            max_gain = 0

            # A. Unclipped internal pairs (O(log N) via Segment Tree)
            if first_idx + 1 <= last_idx - 2:
                max_gain = max(
                    max_gain, query_max(first_idx + 1, last_idx - 2)
                )

            # B. Check ONLY boundary pairs (O(1) lookups instead of O(N) loop)
            boundary_candidates = {first_idx, last_idx - 1}
            for k in boundary_candidates:
                if 0 <= k < num_zero_blocks - 1:
                    l_start = max(zero_blocks[k][0], ql)
                    l_end = min(zero_blocks[k][1], qr)
                    r_start = max(zero_blocks[k + 1][0], ql)
                    r_end = min(zero_blocks[k + 1][1], qr)

                    if l_start <= l_end and r_start <= r_end:
                        gain = (l_end - l_start + 1) + (r_end - r_start + 1)
                        max_gain = max(max_gain, gain)

            res.append(total_ones + max_gain)

        return res