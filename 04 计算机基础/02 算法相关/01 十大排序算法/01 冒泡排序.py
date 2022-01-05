"""
1.比较相邻的元素，如果第一个比第二个大，就交换它们两个；
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，最后的元素是最大的数；
3.针对所有的元素重复以上的步骤，除了最后一个；
重复步骤1~3，直到排序完成。
"""
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            # 从小到大排序
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == '__main__':
    print(bubble_sort([3, 4, 12, 44, 97, 53, 2, 1]))
