# 示例1
for item in [1, 2, 3]:
    if item % 2 == 0:
        break
    print('then')
else:
    print('else')

# 示例2
flag = True
for item in [1, 2, 3]:
    if item % 2 == 0:
        flag = False
        break
    print('then')

if flag:
    print('else')

# 示例3
for item in [1, 2, 3]:
    if item % 2 == 0:
        break
    else:
        print('then')
