# 示例1
# for ...else 如果不被break中断，就执行else子句里的内容
for item in [1, 2, 3]:
    if item % 2 == 0:
        break
    print('then')
else:
    print('else')

# 示例2
# 使用标记，状态为True
flag = True
for item in [1, 2, 3]:
    if item % 2 == 0:
        flag = False
        break
    print('then')

if flag:
    print('else')

# 示例3
#
for item in [1, 2, 3]:
    if item % 2 == 0:
        break
    else:
        print('then')
