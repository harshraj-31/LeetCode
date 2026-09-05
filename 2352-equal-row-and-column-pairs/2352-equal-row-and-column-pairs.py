class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        count = 0

        for row in grid:
            for j in range(n):
                column = []

                for i in range(n):
                    column.append(grid[i][j])

                if row == column:
                    count += 1

        return count