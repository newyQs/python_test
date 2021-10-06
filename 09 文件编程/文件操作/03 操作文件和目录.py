import os
import shutil

# 1.检查文件是否存在
# flag = os.path.exists('./io/04 collections.txt')  # 返回True或者False
# print(flag)

# 1.1 通常在写文件时，我们有必要检查文件是否存在
# if not os.path.exists('./io/test2.txt'):
#     with open('./io/test2.txt', 'w', encoding='utf-8') as f:
#         f.write('Hello 中国')
# else:
#     print('文件已存在，请更换文件名')

# 1.2 删除文件
# if os.path.exists('./io/test2.txt'):
#     os.remove('./io/test2.txt')
#     print('已成功删除')
# else:
#     print('要删除的文件不存在！')

# 1.3重命名文件
# if os.path.exists('./io/test2.txt') and not os.path.exists('./io/tets1.txt'):
#     os.rename('./io/test2.txt', './io/test1.txt')
#     print('已成功重命名')
# else:
#     print('命名冲突了，请更换文件名！')

# 2.操作目录的函数
# 2.1查看当前目录的全路径
# print(os.path.abspath('.'))  # .号即表示当前文件的路径

# 2.2在已存在的目录下创建一个新的目录
# os.mkdir('./io/tt')

# 2.3删除一个空的目录
# os.rmdir('./io/tt')

# 2.4删除一个非空目录，创建多级目录？？

# 3.操作文件名和目录名的函数
# 3.1 拆分路径名
allfilepath = "d:/img/head/ruhua.png"  # 不要求系统中存在该路径，拆分的仅仅是字符串
print(os.path.split(allfilepath))  # 返回值为 ('d:/img/head', 'ruhua.png')

# 3.2获取文件扩展名
allfilepath = "d:/img/head/ruhua.png"  # 不要求系统中存在该路径，拆分的仅仅是字符串
print(os.path.splitext(allfilepath))  # 返回值为 ('d:/img/head/ruhua', '.png')

# 4.使用shutil操作文件和路径
# shutil.copy("d:/04 collections.txt", "d:/testcp.txt")  # 拷贝文件
# shutil.rmtree("d:/testdir")  # testdir 是非空文件夹

# 当然即使我们不使用 shutil 模块，使用 Python 提供的 os 模块也可以实现拷贝文件，删除非空文件夹等等所有的对文件的操作，其实 shutil 模块里面也是调用 os 模块来完成这些复杂的文件操作
