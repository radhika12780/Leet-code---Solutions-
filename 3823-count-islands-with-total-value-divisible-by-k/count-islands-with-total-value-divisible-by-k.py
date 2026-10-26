class Solution:
    def countIslands(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        total_islands = 0

        # Directions for moving up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                # Found unvisited land
                if grid[i][j] > 0:
                    island_sum = 0
                    queue = [(i, j)]
                    
                    # Add starting cell value and mark visited by setting to 0
                    island_sum += grid[i][j]
                    grid[i][j] = 0

                    # BFS to traverse the entire island
                    while queue:
                        r, c = queue.pop(0)

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            # Check boundaries and if cell is land
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))

                    # Check if total island value is divisible by k
                    if island_sum % k == 0:
                        total_islands += 1

        return total_islands