"""
https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-solution/
"""
from typing import List


# 方法1：暴力枚举
def two_sum1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


print("two_sum1：", two_sum1([2, 5, 5, 11], 10))


# 方法2：哈希表
def two_sum2(nums: List[int], target: int) -> List[int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i

    return []


print("two_sum2：", two_sum2([2, 5, 5, 11], 10))


# 返回这两个数的index
def _test1(nums: List[int], target: int) -> List[int]:
    hash_table = {}  # 用字典代替创建一个hash表，key不重复，value保存的是index
    for index, value in enumerate(nums):  # 轮询列表nums
        if target - value in hash_table:  # 寻找另外一个数，如果找到这个数
            return [hash_table[target - value], index]  # 返回两个数的index
        else:
            hash_table[nums[index]] = index  # 否则就加到hash_table中

    return []


print("_test1：", _test1([2, 5, 5, 5, 11], 10))


# 返回这两个数的value
def _test2(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for index, value in enumerate(nums):
        if target - value in hash_table:
            return [target - value, value]
        else:
            hash_table[value] = index
    return []


print("_test2：", _test2([2, 5, 6, 5, 11], 10))
print("_test2：", _test2([3, 2, 5, 2, 11], 5))
