"""
https://leetcode-cn.com/problems/rotate-image/solution/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/
"""
from typing import List


# 方法一：使用辅助数组
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
    matrix_new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_new[j][n - i - 1] = matrix[i][j]
    # 不能写成 matrix = matrix_new
    matrix[:] = matrix_new


# 方法二：原地旋转
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


# 方法三：用翻转代替旋转
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # 水平翻转
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    # 主对角线翻转
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
