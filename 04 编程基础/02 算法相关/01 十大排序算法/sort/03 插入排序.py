"""
一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
1.从第一个元素开始，该元素可以认为已经被排序；
2.取出下一个元素，在已经排序的元素序列中从后向前扫描；
3.如果扫描序列的元素大于该元素，将序列中元素移到下一位置；
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5.将新元素插入到该位置后；
重复步骤2~5。
"""
from typing import List


def insert_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        curr = arr[i]
        j = i
        while j > 0 and arr[j - 1] > curr:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = curr

    return arr


def insertion_sort(arr):
    # 第一层for表示循环插入的遍数
    for i in range(1, len(arr)):
        # 设置当前需要插入的元素
        current = arr[i]
        # 与当前元素比较的比较元素
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            arr[pre_index + 1] = arr[pre_index]
            # 往前选择下一个比较元素
            pre_index -= 1
        # 当比较元素小于当前元素，则将当前元素插入在 其后面
        arr[pre_index + 1] = current
    return arr


if __name__ == '__main__':
    ret = insert_sort([13, 4, 2, 56, 34, 22])
    print(ret)
