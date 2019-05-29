# 两数之和 II - 输入有序数组
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

# 说明:

# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1, 2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
# MY SOLUTION
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         start = 0
#         end = len(numbers) - 1
#         while start < end:
#             temp = numbers[start] + numbers[end]
#             if temp == target:
#                 return [start + 1, end + 1]
#             elif temp < target:
#                 start += 1
#             else:
#                 end -= 1

# BEST SOLUTION
from typing import List


class Solution():
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = {}
        for i, v in enumerate(numbers):
            temp = target - v
            if temp in index:
                return [index[temp], i + 1]
            else:
                index[v] = i + 1


if __name__ == "__main__":
    soul = Solution()
    print(soul.twoSum([0,0,1], 0))
