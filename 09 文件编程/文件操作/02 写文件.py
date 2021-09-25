# 1.写文件
f = open("./io/collect.txt", "w")
f.write("hello nihao")
f.close()

# 2.多次写入
# f.write()：多次写入
# f.seek(index)：从index位置写入
f = open("./io/collect.txt", "w")
f.write("nihao shijie")
f.write("byebye")  # 在上次写入内容的最后面（e）写入 "byebye"
f.seek(1)
f.write("haha")  # 会从 "i" 位置开始往后写如 "haha"
f.close()

# 3.正确调用close方法

# 4.使用flush方法

# 5.在文件后面追加内容


# 总结：
'''
1.文件标识符
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (弃用)

2.open(name,[,mode,buffering])函数
    open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True
模式：
    r       读文件内容。文件指针放在文件的开头，默认方式
    rb      二进制只读。
    w       写文件内容。文件存在，删除原内容重新写入，文件不存在，会重新创建
    wb      二进制写入。
    a       追加文件内容。
    ab      二进制追加。
    
    r+      读写文件内容。文件指针放在文件的开头
    rb+     二进制读写。
    w+      读写文件内容。
    wb+     二进制读写。
    a+      读写文件内容。
    ab+     二进制追加。
    
    t       文本模式（默认）
    x       写模式，文件存在则会报错
    b       二进制模式
    +       读写模式
 
3.读写中的方法
    read(k)
    readline()
    readlines()

    write()
    writelines()
    seek()
    tell()
    flush()

    close()

    readable()
    seekable()
    writeable()

    fileno()
    isatty()
    truncate()

4.with()语句

5.概念性知识


'''

