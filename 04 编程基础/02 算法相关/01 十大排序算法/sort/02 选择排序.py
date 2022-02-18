"""
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。

选择排序为啥不是稳定性排序呢，举个例子：数组 6、7、6、2、8，在对其进行第一遍循环的时候，会将第一个位置的6与后面的2进行交换。
此时，就已经将两个6的相对前后位置改变了。因此选择排序不是稳定性排序算法。
"""
from typing import List


def select_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]

    return arr


def selection_sort(arr):
    # 第一层for表示循环选择的遍数
    for i in range(len(arr) - 1):
        # 将起始元素设为最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
        # 查找一遍后将最小元素与起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


if __name__ == '__main__':
    ret = select_sort([1, 22, 13, 42, 63, 21, 53, 52])
    print(ret)
