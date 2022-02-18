"""
https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
"""


# 方法一：回溯
def permute(nums):
    def backtrack(first=0):
        # 所有数都填完了
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            # 动态维护数组
            nums[first], nums[i] = nums[i], nums[first]
            # 继续递归填下一个数
            backtrack(first + 1)
            # 撤销操作
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    res = []
    backtrack()
    return res
