from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()  # Columns where queens are placed
        posDiag = set()  # Positive diagonals (r + c)
        negDiag = set()  # Negative diagonals (r - c)

        res = []
        board = [["."] * n for _ in range(n)]  # Initialize the board

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

# Example usage for 8-Queens problem
solution = Solution()
n = 8  # Change this value to 8 for the 8-Queens problem
result = solution.solveNQueens(n)

# Print the number of solutions
print(f"Number of solutions for {n}-Queens problem: {len(result)}")

# Print the first solution as an example
if result:
    for row in result[0]:
        print(row)
