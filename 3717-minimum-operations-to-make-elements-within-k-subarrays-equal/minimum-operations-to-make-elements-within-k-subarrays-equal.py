class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}

        cnt = [0] * (m + 1)   # Fenwick tree: count
        sm = [0] * (m + 1)    # Fenwick tree: sum

        def update(i, c, v):
            while i <= m:
                cnt[i] += c
                sm[i] += v
                i += i & -i

        def query(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        LOG = 1
        while LOG * 2 <= m:
            LOG *= 2

        def kth(t):  # t-th smallest ka rank
            pos = 0
            step = LOG
            while step:
                nxt = pos + step
                if nxt <= m and cnt[nxt] < t:
                    pos = nxt
                    t -= cnt[nxt]
                step >>= 1
            return pos + 1

        # cost[i] = window nums[i:i+x] ko equal banane ka min cost
        cost = [0] * (n - x + 1)
        total = 0
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                r = kth((x + 1) // 2)
                med = vals[r - 1]
                c, s = query(r)
                cost[i - x + 1] = med * c - s + (total - s) - med * (x - c)

        # DP: dp[i] = pehle i elements se j subarrays ka min cost
        INF = float('inf')
        prev = [0] * (n + 1)  # j = 0
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]