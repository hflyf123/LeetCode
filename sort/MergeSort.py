# 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
#
# 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
#
# 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
#
# 重复步骤 3 直到某一指针达到序列尾；
#
# 将另一序列剩下的所有元素直接复制到合并序列尾。


from typing import List


def merge(nums: [int]) -> List[int]:
    if len(nums) < 2:
        return nums
    middle = len(nums) // 2
    left = nums[0: middle].copy()
    right = nums[middle:].copy()
    return merge_sort(merge(left), merge(right))


def merge_sort(left: List[int], right: List[int]) -> List[int]:
    print("当前排序的数组是：", left, "和", right)
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while len(left) > 0:
        result.append(left.pop(0))

    while len(right) > 0:
        result.append(right.pop(0))
    return result


if __name__ == '__main__':
    print(merge([5, 4, 1, 3, 2, 6, 7, 8]))
