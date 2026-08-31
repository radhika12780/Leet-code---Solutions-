class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        
        first_idx = -1
        prev_idx = -1
        idx = 1
        
        min_dist = float('inf')
        
        while curr and curr.next:
            is_max = curr.val > prev.val and curr.val > curr.next.val
            is_min = curr.val < prev.val and curr.val < curr.next.val
            
            if is_max or is_min:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                
                prev_idx = idx
            
            prev = curr
            curr = curr.next
            idx += 1
            
        if first_idx == -1 or prev_idx == first_idx:
            return [-1, -1]
            
        max_dist = prev_idx - first_idx
        return [min_dist, max_dist]