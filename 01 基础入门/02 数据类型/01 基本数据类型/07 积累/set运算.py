"""
交集 & : x&y，返回一个新的集合，包括同时在集合 x 和y中的共同元素。

并集 | : x|y，返回一个新的集合，包括集合 x 和 y 中所有元素。

差集 - : x-y，返回一个新的集合,包括在集合 x 中但不在集合 y 中的元素。

补集 ^ : x^y，返回一个新的集合，包括集合 x 和 y 的非共同元素。

"""

x = set('eleven')
y = set('twelve')

print(x & y)  # 交集
print(x.intersection(y))

print(x | y)  # 并集
print(x.union(y))

print(x - y)  # 差集
print(x.difference(y))

print(y - x)  # 差集
print(y.difference(x))

print(x ^ y)  # 补集
print(x.symmetric_difference(y))

print(y ^ x)  # 补集
print(y.symmetric_difference(x))

"""
### 增加
def add(self, element: _T) -> None: ...
def update(self, *s: Iterable[_T]) -> None: ...

### 删除
def discard(self, element: _T) -> None: ...
def pop(self) -> _T: ...
def remove(self, element: _T) -> None: ...

### 清空
def clear(self) -> None: ...

### 浅拷贝
def copy(self) -> Set[_T]: ...

### 差集
def difference(self, *s: Iterable[object]) -> Set[_T]: ...
def difference_update(self, *s: Iterable[object]) -> None: ...

### 交集
def intersection(self, *s: Iterable[object]) -> Set[_T]: ...
def intersection_update(self, *s: Iterable[Any]) -> None: ...

### 补集
def symmetric_difference(self, s: Iterable[_T]) -> Set[_T]: ...
def symmetric_difference_update(self, s: Iterable[_T]) -> None: ...

### 并集
def union(self, *s: Iterable[_T]) -> Set[_T]: ...

### 判断
def isdisjoint(self, s: Iterable[Any]) -> bool: ...
  A.isdisjoint(B)  ==> 判断A和B是否存在交集，存在False，不存在True
def issubset(self, s: Iterable[Any]) -> bool: ...
  A.issubset(B)    ==> 判断A是否是B的子集合
def issuperset(self, s: Iterable[Any]) -> bool: ...
  .issuperset(B)   ==> 判断A是否是B的父集合

"""

print(set({"a": 1}.items()).issubset(set({"a": 1, "b": 2}.items())))
