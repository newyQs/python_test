from typing import List


# 方法一：动态规划
def trap(height: List[int]) -> int:
    if not height:
        return 0

    n = len(height)
    leftMax = [height[0]] + [0] * (n - 1)
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i])

    rightMax = [0] * (n - 1) + [height[n - 1]]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i])

    ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
    return ans


# 方法二：单调栈
def trap2(height: List[int]) -> int:
    ans = 0
    stack = list()
    n = len(height)

    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            left = stack[-1]
            currWidth = i - left - 1
            currHeight = min(height[left], height[i]) - height[top]
            ans += currWidth * currHeight
        stack.append(i)

    return ans
