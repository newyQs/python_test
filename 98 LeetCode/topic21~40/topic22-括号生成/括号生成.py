from typing import List


# 方法一：暴力法
def generate_parenthesis(n: int) -> List[str]:
    def generate(A):
        if len(A) == 2 * n:
            if valid(A):
                ans.append("".join(A))
        else:
            A.append('(')
            generate(A)
            A.pop()
            A.append(')')
            generate(A)
            A.pop()

    def valid(A):
        bal = 0
        for c in A:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0: return False
        return bal == 0

    ans = []
    generate([])
    return ans


# 方法二：回溯法
def generate_parenthesis2(n: int) -> List[str]:
    ans = []

    def backtrack(S, left, right):
        if len(S) == 2 * n:
            ans.append(''.join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S, left, right + 1)
            S.pop()

    backtrack([], 0, 0)
    return ans


# 方法三：按括号序列的长度递归
@lru_cache(None)
def generateParenthesis(self, n: int) -> List[str]:
    if n == 0:
        return ['']
    ans = []
    for c in range(n):
        for left in self.generateParenthesis(c):
            for right in self.generateParenthesis(n - 1 - c):
                ans.append('({}){}'.format(left, right))
    return ans
