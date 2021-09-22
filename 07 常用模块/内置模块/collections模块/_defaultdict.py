from collections import defaultdict

# defaultdict是dict的子类，为不存在的键提供默认值
colors = defaultdict(int)

print(colors['orange'])
print(colors)

language_found = defaultdict(int)
print(language_found['golang'])
