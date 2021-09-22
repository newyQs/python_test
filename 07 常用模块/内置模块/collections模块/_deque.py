from collections import deque

deq = deque('abcdefg')

mylist = [item.upper() for item in deq]
print(mylist)

print(dir(deq))
'''
['append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 'index', 
'insert', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate']
'''
print(dir(mylist))
'''
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
# 除了没有list的sort方法，deque其他方法都有，并且有自己额外的方法
# append和appendleft

# extend和extendleft

# pop和popleft


deq.rotate(1)
print(deq)
