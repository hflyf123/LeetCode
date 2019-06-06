# 3.1 算法步骤
# 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
#
# 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
from typing import List


def insert_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i
        while j > 0 and tmp < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        if j != i:
            nums[j] = tmp
    return nums


if __name__ == '__main__':
    print(insert_sort([5, 4, 3, 2, 1]))
