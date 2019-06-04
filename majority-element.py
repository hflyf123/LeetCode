# 求众数
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache_dict = {}
        for i in nums:
            if i not in cache_dict:
                cache_dict[i] = 1
            else:
                cache_dict[i] += 1
        max = 0
        key = 0
        for k, v in cache_dict.items():
            if v > max:
                max = v
                key = k
        if cache_dict[key] > len(nums) / 2:
            return key


#BEST SOLUTION

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         result = {}
#         for i in set(nums):
#             result[i] = nums.count(i)
#         for key, value in result.items():
#             if value > len(nums)/2:
#                 return key
if __name__ == '__main__':
   soul = Solution()
   print(soul.majorityElement([2,2,1,1,1,2,2]))