from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        fresh_count = 0
        
        # Step 1: Scan the grid to find all initially rotten oranges and count the fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # If there are no fresh oranges to begin with, it takes 0 minutes
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 2: Run BFS level by level (minute by minute)
        while queue and fresh_count > 0:
            minutes += 1
            
            # Process all currently rotten oranges for this exact minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Check all 4 surrounding cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If the neighbor is inside the grid and is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # It becomes rotten
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        # Step 3: Check if any fresh oranges survived
        if fresh_count == 0:
            return minutes
        else:
            return -1