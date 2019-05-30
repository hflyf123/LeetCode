#   长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

# 示例: 

# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 进阶:

# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
from typing import List

# o(n)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sum_all = 0
        nums_len = len(nums)
        min_len = nums_len + 1
        while l < nums_len:
            if r < nums_len and sum_all < s:
                sum_all += nums[r]
                r += 1
            else:
                sum_all -= nums[l]
                l += 1
            if sum_all >= s:
                min_len = min(min_len, r - l)
        if min_len == nums_len + 1:
            return 0
        return min_len        


if __name__ == "__main__":
    soul = Solution()
    print(soul.minSubArrayLen(7, [1, 3, 4, 5]))