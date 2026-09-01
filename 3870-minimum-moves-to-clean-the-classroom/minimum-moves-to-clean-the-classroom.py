from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        rows = len(classroom)
        cols = len(classroom[0])
        
        start_row, start_col = -1, -1
        litter_map = {}
        litter_count = 0
        
        # Map start cell 'S' and litter positions 'L'
        for r in range(rows):
            for c in range(cols):
                ch = classroom[r][c]
                if ch == 'S':
                    start_row, start_col = r, c
                elif ch == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
        
        target_mask = (1 << litter_count) - 1
        
        # Handle case where start position has litter
        start_mask = 0
        if (start_row, start_col) in litter_map:
            start_mask |= (1 << litter_map[(start_row, start_col)])
        
        # 3D matrix for pruning: max remaining energy at (row, col, mask)
        max_energy = [[[-1] * (1 << litter_count) for _ in range(cols)] for _ in range(rows)]
        
        # Queue state: (row, col, mask, current_energy, steps)
        queue = deque([(start_row, start_col, start_mask, energy, 0)])
        max_energy[start_row][start_col][start_mask] = energy
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c, mask, cur_energy, steps = queue.popleft()
            
            if mask == target_mask:
                return steps
            
            if cur_energy == 0:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    next_energy = cur_energy - 1
                    next_mask = mask
                    
                    if cell == 'L':
                        bit_idx = litter_map[(nr, nc)]
                        next_mask |= (1 << bit_idx)
                    
                    if cell == 'R':
                        next_energy = energy
                    
                    if next_energy > max_energy[nr][nc][next_mask]:
                        max_energy[nr][nc][next_mask] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, steps + 1))
        
        return -1