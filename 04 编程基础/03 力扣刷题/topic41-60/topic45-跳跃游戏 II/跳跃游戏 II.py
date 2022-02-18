"""
https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
"""
from typing import List


# 方法一：反向查找出发位置

# 方法二：正向查找可到达的最大位置
def jump(nums: List[int]) -> int:
    n = len(nums)
    maxPos, end, step = 0, 0, 0
    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
    return step
