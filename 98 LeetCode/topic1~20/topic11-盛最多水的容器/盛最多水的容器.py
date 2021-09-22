from typing import List


# 时间复杂度： O(n); 空间复杂度： O(1)
def max_area(height: List[int]) -> int:
    # 初始化双指针
    i, j = 0, len(height) - 1
    maxarea = 0
    # 循环遍历, 求面积注意：h是高， w是宽， h应该是 height[i] height[j]中的”矮“的~不然水就漏了~
    # 谁比较“矮”谁优先
    while i < j:
        if height[i] > height[j]:
            h, w = height[j], j - i
            j -= 1
        else:
            h, w = height[i], j - i
            i += 1
        maxarea = max(maxarea, h * w)
    return maxarea
