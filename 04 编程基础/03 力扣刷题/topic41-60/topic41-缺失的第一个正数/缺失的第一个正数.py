from typing import List


# 方法一：哈希表
def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1

    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1


# 方法二：置换
def firstMissingPositive2(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
