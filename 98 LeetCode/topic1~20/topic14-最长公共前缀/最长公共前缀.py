from typing import List


# 方法1：横向扫描
def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix, count = strs[0], len(strs)
    for i in range(1, count):
        prefix = lcp(prefix, strs[i])
        if not prefix:
            break

    return prefix


def lcp(str1, str2):
    length, index = min(len(str1), len(str2)), 0
    while index < length and str1[index] == str2[index]:
        index += 1
    return str1[:index]


# 方法2：纵向扫描
def longest_common_prefix2(strs: List[str]) -> str:
    if not strs:
        return ""

    length, count = len(strs[0]), len(strs)
    for i in range(length):
        c = strs[0][i]
        if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
            return strs[0][:i]

    return strs[0]


# 方法3：分治
def longest_common_prefix3(strs: List[str]) -> str:
    def lcp(start, end):
        if start == end:
            return strs[start]

        mid = (start + end) // 2
        lcp_left, lcp_right = lcp(start, mid), lcp(mid + 1, end)
        min_length = min(len(lcp_left), len(lcp_right))
        for i in range(min_length):
            if lcp_left[i] != lcp_right[i]:
                return lcp_left[:i]

        return lcp_left[:min_length]

    return "" if not strs else lcp(0, len(strs) - 1)


# 方法4：二分查找
def longest_common_prefix4(strs: List[str]) -> str:
    def is_common_prefix(length):
        str0, count = strs[0][:length], len(strs)
        return all(strs[i][:length] == str0 for i in range(1, count))

    if not strs:    
        return ""

    min_length = min(len(s) for s in strs)
    low, high = 0, min_length
    while low < high:
        mid = (high - low + 1) // 2 + low
        if is_common_prefix(mid):
            low = mid
        else:
            high = mid - 1

    return strs[0][:low]
