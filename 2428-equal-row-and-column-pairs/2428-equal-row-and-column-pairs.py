from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Convert rows and columns to tuples
        row_count = Counter(tuple(row) for row in grid)
        col_count = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))

        # Count matching row and column pairs
        return sum(row_count[row] * col_count[row] for row in row_count)
      