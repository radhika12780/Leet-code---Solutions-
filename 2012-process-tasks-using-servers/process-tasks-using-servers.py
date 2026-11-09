import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        # free_servers stores tuples of (weight, index)
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # busy_servers stores tuples of (free_time, weight, index)
        busy_servers = []
        
        ans = []
        current_time = 0
        
        for task_idx, task_time in enumerate(tasks):
            # Advance time if task arrives later than current_time
            current_time = max(current_time, task_idx)
            
            # If no free servers are available, jump time to when the earliest server becomes free
            if not free_servers:
                current_time = max(current_time, busy_servers[0][0])
            
            # Move all servers that are finished by current_time back to free_servers
            while busy_servers and busy_servers[0][0] <= current_time:
                free_time, weight, server_idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, server_idx))
            
            # Assign task to the server with smallest weight (and smallest index on tie)
            weight, server_idx = heapq.heappop(free_servers)
            ans.append(server_idx)
            
            # Push to busy_servers with the calculated completion time
            heapq.heappush(busy_servers, (current_time + task_time, weight, server_idx))
            
        return ans