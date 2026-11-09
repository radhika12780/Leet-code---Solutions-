from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        # 1. Store original indices of queries to maintain output order
        # queries_with_idx[i] = (query_time, original_index)
        q_len = len(queries)
        sorted_queries = sorted([(queries[i], i) for i in range(q_len)])
        
        # 2. Sort logs based on time (logs[i] = [server_id, time])
        logs.sort(key=lambda item: item[1])
        
        ans = [0] * q_len
        server_counts = defaultdict(int)
        active_servers_count = 0
        
        left = 0
        right = 0
        total_logs = len(logs)
        
        # 3. Process each query using sliding window
        for q_time, original_idx in sorted_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand window: Add logs that occur <= window_end
            while right < total_logs and logs[right][1] <= window_end:
                s_id = logs[right][0]
                if server_counts[s_id] == 0:
                    active_servers_count += 1
                server_counts[s_id] += 1
                right += 1
            
            # Shrink window: Remove logs that occurred before window_start
            while left < total_logs and logs[left][1] < window_start:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    active_servers_count -= 1
                left += 1
            
            # Servers with zero requests = Total servers - Active servers in window
            ans[original_idx] = n - active_servers_count
            
        return ans