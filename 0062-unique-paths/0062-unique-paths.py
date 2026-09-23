class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D array of size n with all 1s.
        # (There is only 1 way to reach any cell in the very first row: keep going right)
        row = [1] * n
        
        # Process every row from the second row down to the last row
        for i in range(1, m):
            # For each cell in the row (skipping the first column since it's always 1)
            for j in range(1, n):
                # The number of ways to reach the current cell is the sum of:
                # 1. The ways to reach the cell directly ABOVE it (currently stored in row[j])
                # 2. The ways to reach the cell directly to the LEFT of it (row[j-1])
                row[j] = row[j] + row[j - 1]
                
        # The last element in the row is the bottom-right corner
        return row[-1]