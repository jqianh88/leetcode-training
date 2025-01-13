'''
Steps:

Use a decision tree to place one queen per row.
Prune invalid placements (same column, diagonal).
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Restate: Given a particular n, return all distinct solution so that a Q (queen)
        is not in the same row or column.

        Algorithm: Backtracking
        Time Complexity: O(K^N)
        Space Complexity: O(M)

        Pseudo:
        - initialize result
        - initialize board with all "."
        - method of is_valid
            - for loop through the index of row
                - return False if board[i][col] == "Q" or \
               (col - (row - i) >= 0 and board[i][col - (row - i)] == "Q") or \
               (col + (row - i) < n and board[i][col + (row - i)] == "Q"):
            - return True

        - backtrack method
            base case:
            - if row == n:
                append(["".join(r) for r in board])
                return

            option case:
            - for col in range(n)
                if is_valid(row, col)
                    set the position as Q
                    backtrack(row + 1)
                    undo the placement by setting the position back to "."
        call backtrack(0)
        return result
       '''
        result = []
        board = [["." for _ in range(n)] for row in range(n)]

        def is_valid(row: int, col: int) -> bool:
            for i in range(row):
                if board[i][col] == "Q" or (col - (row-i) >=0 and board[i][col - (row-i)] == "Q") or (col + (row-i) < n and board[i][col + (row-i)] == "Q"):
                    return False
            return True

        def backtrack(row: int) -> None:
            # Base case
            if row == n:
                result.append(["".join(r) for r in board])
                return

            # Options cases
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
        backtrack(0)
        return result