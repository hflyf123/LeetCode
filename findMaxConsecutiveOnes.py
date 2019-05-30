# 最大连续1的个数
# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 注意：
#
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        temp_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp_max += 1
            elif temp_max != 0:
                res = max(res, temp_max)
                temp_max = 0
        res = max(res, temp_max)
        return res


# BEST SOLUTION
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         count = 0
#         cmax = 0
#         for num in nums:
#             if num == 1:
#                 count += 1
#             else:
#                 if count > cmax:
#                     cmax = count
#                 count = 0
#         return cmax if cmax > count else count


if __name__ == '__main__':
    soul = Solution()
    print(soul.findMaxConsecutiveOnes([0,1]))