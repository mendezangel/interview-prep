# Determine if a 9 x 9 sudoku board is valid. Only the filled cells need to be validated according to
# the following rules:
# Each row must contain the digits 1-9 without repetition
# each column must contain the digits 1-9 without repetition.
# each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# a sudoku board (partially filled) could be valid but is not necessarily solvable.
# only the filled cells need to be validated according to the mentioned rules

class Solution:
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        pass
            


board_one = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

# board_two = [["8","3",".",".","7",".",".",".","."]
#              ["6",".",".","1","9","5",".",".","."],
#              [".","9","8",".",".",".",".","6","."],
#              ["8",".",".",".","6",".",".",".","3"],
#              ["4",".",".","8",".","3",".",".","1"],
#              ["7",".",".",".","2",".",".",".","6"],
#              [".","6",".",".",".",".","2","8","."],
#              [".",".",".","4","1","9",".",".","5"],
#              [".",".",".",".","8",".",".","7","9"]]

solution = Solution()
print(solution.is_valid_sudoku(board_one)) # True
# print(solution.is_valid_sudoku(board_two)) # False