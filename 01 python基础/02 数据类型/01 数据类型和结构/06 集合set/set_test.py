# s = {"a", "v", [1, 2, 3]}
"""
set有2个特点：
1. 集合的值必须是可hash的，即不可变类型
2. 集合的值是不重复的;
3. 集合内部的值是无序的；

集合的增删改查方法：
add(val) -->None
update([val1,value2,...])

pop()
remove(val)-->None


"""

s = {"a", "b", "c", 1, 4, (1, 2)}

ret = s.add("abc")
print(ret)  # None
print(s)

####################################################
s = {"a", "b", "c", 1, 4, (1, 2)}

ret = s.pop()

print(ret)
print(s)

####################################################
s = {"a", "b", "c", 1, 4, (1, 2)}

ret = s.update("dg", "ef")
# ret = s.update(["dd", "ee"])
print(ret)
print(s)

####################################################
s = {"a", "b", "c", 1, 4, (1, 2)}

ret = s.remove("a")
print(ret)  # None
print(s)

####################################################
s = {"a", "b", "c", 1, 4, (1, 2)}

ret = s.copy()
ret.add("111111111")
print(ret)
print(s)

####################################################
s = {"a", "b", "c", 1, 4, (1, 2)}

ret = s.clear()  # None
print(ret)
print(s)


