from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        rows = len(maze)
        cols = len(maze[0])
        
        start_row, start_col = entrance
        
        # Queue stores: (current_row, current_col, current_distance)
        queue = deque([(start_row, start_col, 0)])
        
        # Mark the entrance as a wall to indicate we've visited it
        maze[start_row][start_col] = '+'
        
        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, dist = queue.popleft()
            
            # Try moving in all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the next step is within bounds and is an empty space
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    
                    # If this empty space is on the border, it's an exit!
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return dist + 1
                    
                    # Otherwise, mark it as visited by turning it into a wall
                    maze[nr][nc] = '+'
                    
                    # Add it to the queue to explore later
                    queue.append((nr, nc, dist + 1))
                    
        # If the queue empties and we never returned, no exit was found
        return -1