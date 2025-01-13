
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


Pseudo:
 - is_valid:
    - for loop through range(9) to check that for numbers 1-9 if the current row, col, or 3 x3 has that value already ([row//3 * 3+i//3][col//3*3+i%3]) --> return False
    Return True
- backtrack
    - for loop through row
        - for loop through col
            - if current position's value is "."
                - for loop from 1 to 10
                    check if is_valid
                        set the position's value to str(num)
                        - if backtrack
                            return True
                        - undo the assignment
                return False
    return True
call backtrack()



Precomputed Empty Cells:

Instead of iterating over all cells on each recursive call, we maintain a list of empty cells (empty_cells). This reduces redundant looping over filled cells, focusing only on the unfilled ones.
Index Tracking for Backtracking:

Use an index to track the current cell being solved. This ensures that we handle each empty cell only once during recursion.
Streamlined Validation:

Validation of constraints (rows, cols, and subgrids) is performed only when placing a number. This keeps each operation at constant time O(1).
Early Exit:

If all empty cells are filled (index == len(empty_cells)), we immediately return True, terminating further recursion.

'''


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]
        empty_cells = []

        # Precompute constraints and empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrids[(r // 3) * 3 + c // 3].add(num)

        def backtrack(index=0):
            # Base case: All empty cells are filled
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            subgrid_index = (r // 3) * 3 + c // 3

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in subgrids[subgrid_index]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrids[subgrid_index].add(num)

                    # Recur to the next cell
                    if backtrack(index + 1):
                        return True

                    # Undo the placement
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    subgrids[subgrid_index].remove(num)

            return False

        backtrack()
