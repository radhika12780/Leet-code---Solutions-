class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        # 1. Adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. Binary Lifting for LCA & Euler Tour setup
        LOG = 16  # 2^16 > 50000
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        timer = 1

        # Iterative DFS to avoid hitting Python's recursion limit
        stack = [(0, -1, 0)]
        
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                in_time[u] = timer
                timer += 1
                up[u][0] = p if p != -1 else 0
                for i in range(1, LOG):
                    up[u][i] = up[up[u][i - 1]][i - 1]
                
                stack.append((u, p, 1))
                for v in adj[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                out_time[u] = timer

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # 3. Fenwick Tree (BIT)
        bit = [0] * (timer + 2)

        def update_bit(idx, val):
            while idx < len(bit):
                bit[idx] ^= val
                idx += idx & -idx

        def query_bit(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & -idx
            return res

        # 4. Initialize character bitmasks
        node_masks = [1 << (ord(ch) - ord('a')) for ch in s]
        for i in range(n):
            update_bit(in_time[i], node_masks[i])
            update_bit(out_time[i], node_masks[i])

        # 5. Process updates and queries
        res = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]
                new_mask = 1 << (ord(new_char) - ord('a'))
                diff = node_masks[u] ^ new_mask
                node_masks[u] = new_mask
                
                update_bit(in_time[u], diff)
                update_bit(out_time[u], diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                path_mask = query_bit(in_time[u]) ^ query_bit(in_time[v]) ^ node_masks[lca]
                
                # Path can form a palindrome if at most 1 bit is set
                can_be_palindrome = (path_mask & (path_mask - 1)) == 0
                res.append(can_be_palindrome)

        return res