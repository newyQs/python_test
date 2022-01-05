"""
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。

选择排序为啥不是稳定性排序呢，举个例子：数组 6、7、6、2、8，在对其进行第一遍循环的时候，会将第一个位置的6与后面的2进行交换。
此时，就已经将两个6的相对前后位置改变了。因此选择排序不是稳定性排序算法。
"""
from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]

    return arr


if __name__ == '__main__':
    ret = selection_sort([1, 22, 13, 42, 63, 21, 53, 52])
    print(ret)
