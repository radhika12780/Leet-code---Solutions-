class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        
        # A shift of total_elements is a complete cycle, so we can reduce k
        k = k % total_elements
        
        # If k is 0 after reduction, no shifting is needed
        if k == 0:
            return grid
            
        # Initialize the result grid with zeros matching the dimensions
        result = [[0] * n for _ in range(m)]
        
        # Directly map each element to its new position
        for r in range(m):
            for c in range(n):
                # Calculate the flat 1D index, shift it, and wrap around
                flat_index = r * n + c
                new_flat_index = (flat_index + k) % total_elements
                
                # Convert the new flat index back to 2D row and column indices
                new_r = new_flat_index // n
                new_c = new_flat_index % n
                
                result[new_r][new_c] = grid[r][c]
                
        return result