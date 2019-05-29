# 数组拆分 I
# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

# 示例 1:

# 输入: [1,4,3,2]

# 输出: 4
# 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
# 提示:

# n 是正整数,范围在 [1, 10000].
# 数组中的元素范围在 [-10000, 10000].
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(0, n, 2):
            res += nums[i]
        return res

if __name__ == "__main__":
    soul = Solution()
    print(soul.arrayPairSum([1,4,3,2]))