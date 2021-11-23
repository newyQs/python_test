from collections import OrderedDict

colors = OrderedDict()

colors['orange'] = 'ORANGE'
colors['blue'] = 'BLUE'
colors['green'] = 'GREEN'

tt = [k for k, v in colors.items()]

print(tt)
# 可以按照特定顺序获取键，不过在现版本中，dict默认按照插入顺序
