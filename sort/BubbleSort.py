from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    if nums:
        i = len(nums) - 1
        while i:
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            i -= 1
        return nums
    else:
        return nums


if __name__ == '__main__':
    print(bubble_sort([5, 4, 3, 2, 1]))
