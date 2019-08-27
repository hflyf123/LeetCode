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
        # map存储次数, 时间复杂度o(n),空间复杂度o(n)
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

    # 暴力解法,时间复杂度o(n^2),通过不了
    def majorityElement1(self, nums: List[int]) -> int:
        for item in nums:
            count = nums.count(item)
            if count > len(nums) / 2:
                return item

    # sort,判断重复次数,大于n/2的就是解,o(nlogn)
    def majorityElement2(self, nums: List[int]) -> int:
        sorted_nums = nums.sort()
        times = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                times += 1
            else:
                times = 1
            if times > len(nums)/2:
                return nums[i]
        # 如果只有一個數,那么第一个数就是众数
        return nums[times]

    # 分治做法,如果两边的majority相等,就得出了结果,若是不相同,则比较两边出现次数多的majority
    def majorityElement3(self, nums: List[int]) -> int:
        pass

# BEST SOLUTION
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
    print(soul.majorityElement2([1]))
