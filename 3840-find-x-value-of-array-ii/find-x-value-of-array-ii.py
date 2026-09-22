class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree_size = 1
        while tree_size < n:
            tree_size *= 2
        
        tree = [None] * (2 * tree_size)

        def make_node(val):
            rem = val % k
            counts = [0] * k
            counts[rem] = 1
            return (rem, counts)

        def combine(left, right):
            if left is None:
                return right
            if right is None:
                return left
            
            p1, c1 = left
            p2, c2 = right
            
            merged_prod = (p1 * p2) % k
            merged_counts = list(c1)
            
            for r in range(k):
                if c2[r] > 0:
                    new_r = (p1 * r) % k
                    merged_counts[new_r] += c2[r]
                    
            return (merged_prod, merged_counts)

        # Build initial segment tree
        for i in range(n):
            tree[tree_size + i] = make_node(nums[i])
            
        for i in range(tree_size - 1, 0, -1):
            tree[i] = combine(tree[2 * i], tree[2 * i + 1])

        def update(idx, val):
            pos = tree_size + idx
            tree[pos] = make_node(val)
            pos //= 2
            while pos > 0:
                tree[pos] = combine(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        def query_tree(l, r):
            left_res = None
            right_res = None
            
            l += tree_size
            r += tree_size
            
            while l <= r:
                if l % 2 == 1:
                    left_res = combine(left_res, tree[l])
                    l += 1
                if r % 2 == 0:
                    right_res = combine(tree[r], right_res)
                    r -= 1
                l //= 2
                r //= 2
                
            return combine(left_res, right_res)

        ans = []
        for idx, val, start, target_x in queries:
            update(idx, val)
            _, counts = query_tree(start, n - 1)
            ans.append(counts[target_x])

        return ans