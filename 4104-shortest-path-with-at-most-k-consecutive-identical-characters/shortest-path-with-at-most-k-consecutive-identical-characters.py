import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        # Step 1: Build an efficient adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Step 2: Flat state-space allocation via Bit-Packing
        # Shift by 6 bits because k <= 50, which is less than 2^6 (64)
        max_state = (n << 6)
        dist = [float('inf')] * max_state
        
        # Base Case: Node 0 starts with a consecutive sequence length of 1
        start_state = (0 << 6) | 1
        dist[start_state] = 0
        
        # Priority Queue: storing (total_weight, current_node, consecutive_count)
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            # Target reached: Since this is a min-heap, the first time we pop 
            # the destination node, it is guaranteed to be the global minimum.
            if u == n - 1:
                return d
                
            # Outdated state pruning
            if d > dist[(u << 6) | count]:
                continue
                
            u_label = labels[u]
            
            # Step 3: Explore neighbors with fast transition rules
            for v, w in adj[u]:
                # If the neighbor has the same character, increment; otherwise, reset to 1
                next_count = (count + 1) if labels[v] == u_label else 1
                
                # Prune paths that violate the constraint
                if next_count <= k:
                    next_state = (v << 6) | next_count
                    new_dist = d + w
                    
                    # Relaxation step
                    if new_dist < dist[next_state]:
                        dist[next_state] = new_dist
                        heapq.heappush(pq, (new_dist, v, next_count))
                        
        return -1