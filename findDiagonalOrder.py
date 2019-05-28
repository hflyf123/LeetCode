# 对角线遍历
# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。


# 示例:

# 输入:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# 输出:  [1, 2, 4, 7, 5, 3, 6, 8, 9]

# 解释:


# 说明:

# 给定矩阵中的元素总数不会超过 100000 。
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        directions = [(-1, 1), (1, -1)]
        count = 0
        res = []
        i, j = 0, 0
        M, N = len(matrix), len(matrix[0])
        while len(res) < M * N:
            if 0 <= i < M and 0 <= j < N:
                res.append(matrix[i][j])
                direct = directions[count % 2]
                i, j = i + direct[0], j + direct[1]
                continue
            elif i < 0 and 0 <= j < N:
                i += 1
            elif 0 <= i < M and j < 0:
                j += 1
            elif i < M and j >= N:
                i += 2
                j -= 1
            elif i >= M and j < N:
                j += 2
                i -= 1
            count += 1
        return res



# MYSOLUTION
# class Solution:
#     def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         m = len(matrix) - 1
#         if m == -1:
#             return []
#         n = len(matrix[0]) - 1
#         c = m + n + 1
#         l = []
#         for x in range(c + 1):
#             if x % 2 == 0:
#                 for i in range(x, -1, -1):
#                     j = x - i
#                     if i <= m and j <= n:
#                         l.append(matrix[i][j])
#                     elif j > n:
#                         break
#                     else:
#                         continue
#             else:
#                 for j in range(x, -1, -1):
#                     i = x - j
#                     if i <= m and j <= n:
#                         l.append(matrix[i][j])
#                     elif i > m:
#                         break
#                     else:
#                         continue
#         return l


if __name__ == "__main__":
    soul = Solution()
    print(soul.findDiagonalOrder([[2, 3]]))
