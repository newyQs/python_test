"""
1.创建文件
2.创建目录
3.创建多级目录

4.删除文件
5.删除目录
6.删除非空目录

7.复制文件
8.复制目录
"""
import os
import shutil

# 创建文件
open("test.txt", mode='w')

# 创建单级目录
if not os.path.exists("demo"):
    os.mkdir("demo")

# 创建多级目录
if not os.path.exists("ts/demo"):
    os.makedirs("ts/demo")

# 删除文件
if os.path.exists("test.txt"):
    os.remove("test.txt")

# 删除单级目录
if os.path.exists("demo"):
    os.rmdir("demo")

# 删除多级目录
if os.path.exists("t1/t2"):
    os.removedirs("t1/t2")

# 删除整个路径，无论是否为空
shutil.rmtree("")
