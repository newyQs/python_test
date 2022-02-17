from typing import List

# 方法1：暴力枚举
'''
最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x。
当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，因此不需要再进行匹配。
而每一个元素不能被使用两次，所以我们只需要在 x 后面的元素中寻找 target - x。

复杂度分析:
时间复杂度：O(n^2)，其中n是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。
空间复杂度：O(1)。
'''


def two_sum1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


print("two_sum1：", two_sum1([2, 5, 5, 11], 10))

# 方法2：哈希表
'''
注意到方法1的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。
因此，我们需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。
如果存在，我们需要找出它的索引。
使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(n) 降低到 O(1)。
这样我们创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，然后将 x 插入到哈希表中，
即可保证不会让 x 和自己匹配。

复杂度分析
时间复杂度：O(n)，其中 n 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。
空间复杂度：O(n)，其中 n 是数组中的元素数量。主要为哈希表的开销。
'''


def two_sum2(nums: List[int], target: int) -> List[int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i

    return []


print("two_sum2：", two_sum2([2, 5, 5, 11], 10))


# 返回这两个数的index
def _test1(nums: List[int], target: int) -> List[int]:
    hash_table = {}  # 用字典代替创建一个hash表，key不重复，value保存的是index
    for index, value in enumerate(nums):  # 轮询列表nums
        if target - value in hash_table:  # 寻找另外一个数，如果找到这个数
            return [hash_table[target - value], index]  # 返回两个数的index
        else:
            hash_table[nums[index]] = index  # 否则就加到hash_table中

    return []


print("_test1：", _test1([2, 5, 5, 5, 11], 10))


# 返回这两个数的value
def _test2(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for index, value in enumerate(nums):
        if target - value in hash_table:
            return [target - value, value]
        else:
            hash_table[value] = index
    return []


print("_test2：", _test2([2, 5, 6, 5, 11], 10))
print("_test2：", _test2([3, 2, 5, 2, 11], 5))
