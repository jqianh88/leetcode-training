from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = {}
        n = len(grid)

        # Count the frequency of each row
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1

        res = 0

        # Check each column against the row count
        for j in range(n):
            column = tuple(grid[i][j] for i in range(n))
            if column in row_count:
                res += row_count[column]

        return res