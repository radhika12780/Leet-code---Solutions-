class Solution:
    def createGrid(self, m, n):
        grid = []
        
        # Row 0 is completely free
        grid.append('.' * n)
        
        # All remaining rows have obstacles except the very last column
        for _ in range(m - 1):
            grid.append('#' * (n - 1) + '.')
            
        return grid