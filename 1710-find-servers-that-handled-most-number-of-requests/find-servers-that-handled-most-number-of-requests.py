import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        count = [0] * k
        busy = []
        
        available_after = list(range(k))
        heapq.heapify(available_after)
        available_before = []
        
        for i, (start, duration) in enumerate(zip(arrival, load)):
            target = i % k
            
            if target == 0:
                while available_before:
                    heapq.heappush(available_after, heapq.heappop(available_before))
            
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                if server_id >= target:
                    heapq.heappush(available_after, server_id)
                else:
                    heapq.heappush(available_before, server_id)
            
            assigned_server = -1
            if available_after:
                assigned_server = heapq.heappop(available_after)
            elif available_before:
                assigned_server = heapq.heappop(available_before)
            
            if assigned_server != -1:
                count[assigned_server] += 1
                heapq.heappush(busy, (start + duration, assigned_server))
        
        max_requests = max(count)
        return [i for i in range(k) if count[i] == max_requests]