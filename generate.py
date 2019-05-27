# 杨辉三角
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。


# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 5
# 输出:
# [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1]
# ]
from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows < 1:
            return res
        elif numRows == 1:
            res.append([1])
            return res
        elif numRows == 2:
            res.append([1])
            res.append([1, 1])
            return res
        res.append([1])
        res.append([1, 1])
        for i in range(3, numRows + 1):
            temp = []
            for j in range(i):
                if j == 0:
                    temp.append(1)
                elif j == i - 1:
                    temp.append(1)
                else:
                    temp.append(res[i-2][j-1] + res[i-2][j])
            res.append(temp)
        return res


if __name__ == "__main__":
    soul = Solution()
    print(soul.generate(5))


# BEST SOULUTION
