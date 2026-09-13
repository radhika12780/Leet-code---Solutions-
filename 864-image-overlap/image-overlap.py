class Solution:
    def largestOverlap(self, img1, img2):
        # Dono images me jahan 1 hai unke (row, col) positions save karo
        ones1 = []
        ones2 = []
        
        n = len(img1)
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))
                if img2[r][c] == 1:
                    ones2.append((r, c))
        
        # Har shift (r2 - r1, c2 - c1) kitni baar aaya usko count karo
        counts = {}
        max_overlap = 0
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                counts[shift] = counts.get(shift, 0) + 1
                if counts[shift] > max_overlap:
                    max_overlap = counts[shift]
                    
        return max_overlap