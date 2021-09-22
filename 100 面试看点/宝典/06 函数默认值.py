# 如下代码的输出结果
def extend_list(val, lis=[]):
    lis.append(val)

    return lis


li1 = extend_list(10)
li2 = extend_list(123, [])
li3 = extend_list('a')

print(f'li1={li1}')
print(f'li1={li2}')
print(f'li1={li3}')

#
l = []
for i in range(10):
    l.append({'num': i})

# print(l)

L = []
a = {'num': 0}
for i in range(10):
    a['num'] = i
    L.append(a)
