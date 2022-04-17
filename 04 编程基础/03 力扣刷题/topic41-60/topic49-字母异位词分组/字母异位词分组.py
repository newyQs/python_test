"""
https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-CI-fen-zu-by-leetcode-solut-gyoc/
"""
from typing import List
import collections


# 方法一：排序
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    mp = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)

    return list(mp.values())


# 方法二：计数
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    mp = collections.defaultdict(list)

    for st in strs:
        counts = [0] * 26
        for ch in st:
            counts[ord(ch) - ord("a")] += 1
        # 需要将 list 转换成 tuple 才能进行哈希
        mp[tuple(counts)].append(st)

    return list(mp.values())
