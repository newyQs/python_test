# 滑动窗口1
def length_of_longest_substring(s: str) -> int:
    '''字符串中最长且连续的子字符串'''
    occ = set()  # 哈希集合，记录每个字符是否出现过
    n = len(s)
    rk, ans = -1, 0  # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动

    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])  # 左指针向右移动一格，移除一个字符
        while rk + 1 < n and s[rk + 1] not in occ:
            occ.add(s[rk + 1])  # 不断地移动右指针
            rk += 1

        ans = max(ans, rk - i + 1)  # 第 i 到 rk 个字符是一个极长的无重复字符子串
    return ans


print(length_of_longest_substring('abcabcbb'))


# 滑动窗口2
def length_of_longest_substring2(s: str) -> int:
    if not s:
        return 0
    left = 0
    lookup = set()

    max_len = 0
    cur_len = 0
    for i in range(len(s)):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        lookup.add(s[i])
    return max_len


# 滑动窗口3
def length_of_longest_substring3(s: str) -> int:
    from collections import defaultdict
    lookup = defaultdict(int)
    start = 0
    end = 0
    max_len = 0
    counter = 0
    while end < len(s):
        if lookup[s[end]] > 0:
            counter += 1
        lookup[s[end]] += 1
        end += 1
        while counter > 0:
            if lookup[s[start]] > 1:
                counter -= 1
            lookup[s[start]] -= 1
            start += 1
        max_len = max(max_len, end - start)
    return max_len
