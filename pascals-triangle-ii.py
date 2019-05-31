# 杨辉三角 II
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        nums = rowIndex + 1
        result = [1 for c in range(nums)]
        for i in range(nums):
            result[i] = [1] * (i + 1)
        for i in range(2, nums):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        print(result)
        return result[rowIndex]

# BEST SOLUTION
# import copy
# class Solution:
#     def getRow(self, rowIndex: 'int') -> 'List[int]':
#         res = [1 for x in range(rowIndex+1)]
#         pre = [1 for x in range(rowIndex+1)]
#         for i in range(1, rowIndex+1):
#             #res[i] = 1
#             for j in range(1, i):
#                 res[j] = pre[j]+pre[j-1]
#             pre = copy.copy(res)
#         return res


if __name__ == "__main__":
    soul = Solution()
    print(soul.getRow(3))
