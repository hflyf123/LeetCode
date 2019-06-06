from typing import List


def select_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        p_min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[p_min]:
                p_min = j
        nums[p_min], nums[i] = nums[i], nums[p_min]
    return nums


if __name__ == '__main__':
    print(select_sort([5, 4, 3, 2, 1]))
