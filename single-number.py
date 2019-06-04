#
from typing import List


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         buffer_dict = {x: 0 for x in nums}
#         for x in nums:
#             buffer_dict[x] += 1
#         for k, v in buffer_dict.items():
#             if v == 1:
#                 return k

# BEST SOLUTION


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         temp = 0
#         for i in nums:
#             temp ^= i
#         return temp

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)


if __name__ == '__main__':
    soul = Solution()
    print(soul.singleNumber([-1, -1, -2]))
