# 编写一个程序，通过已填充的空格来解决数独问题。

# 一个数独的解法需遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。

# 一个数独。

# 答案被标成红色。

# Note:

# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sudoku-solver
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        self._solve(board)
        
    def _solve(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for c in range(1, 10):
                        if self._is_valid(board, i, j, c):
                            board[i][j] = str(c)
                            if self._solve(board):
                                return True
                            else:
                                board[i][j] = "."  # 还原
            return False
        return True

    def _is_valid(self, board: List[List[str]], row: int, col: int, c: int) -> bool:
        for i in range(len(board)):
            if board[row][i] != "." and board[row][i] == c:
                return False
            if board[i][col] != "." and board[i][col] == c:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != "." and board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True

if __name__ == "__main__":
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    so = Solution()
    so.solveSudoku(board)
    print(board)
        
        
                            
