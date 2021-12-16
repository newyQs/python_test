"""
https://liujiangblog.com/

'chown', 'collections', 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree', 'disk_usage',
'errno', 'fnmatch', 'get_archive_formats', 'get_terminal_size', 'get_unpack_formats', 'getgrnam', 'getpwnam',
'ignore_patterns', 'make_archive', 'move', 'nt', 'os', 'posix', 'register_archive_format', 'register_unpack_format',
'rmtree', 'stat', 'sys', 'unpack_archive', 'unregister_archive_format', 'unregister_unpack_format', 'which'
"""
import shutil

# 1. shutil.copyfileobj(fsrc, fdst[, length=16*1024])
# copy文件内容到另一个文件，可以copy指定大小的内容。这个方法是shutil模块中其它拷贝方法的基础，其它方法在本质上都是调用这个方法。
shutil.copyfileobj()

# 2. shutil.copyfile(src, dst)
# 拷贝整个文件。
shutil.copyfile()

# 3. shutil.copymode(src, dst)
# 仅拷贝权限。内容、组、用户均不变。
shutil.copymode()

# 4. shutil.copystat(src, dst)
# 仅复制所有的状态信息，包括权限，组，用户，时间等。

# 5. shutil.copy(src,dst)
# 同时复制文件的内容以及权限，也就是先copyfile()然后copymode()。

# 6. shutil.copy2(src, dst)
# 同时复制文件的内容以及文件的所有状态信息。先copyfile()后copystat()。

# 7. shutil.ignore_patterns(*patterns)
# 忽略指定的文件。通常配合下面的copytree()方法使用。

# 8. shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,ignore_dangling_symlinks=False)
# 递归地复制目录及其子目录的文件和状态信息
# symlinks：指定是否复制软链接。小心陷入死循环。
# ignore：指定不参与复制的文件，其值应该是一个ignore_patterns()方法。
# copy_function：指定复制的模式

# 9. shutil.rmtree(path[, ignore_errors[, onerror]])
# 递归地删除目录及子目录内的文件。注意！该方法不会询问yes或no，被删除的文件也不会出现在回收站里，请务必小心！

# 10. shutil.move(src, dst)
# 递归地移动文件，类似mv命令，其实就是重命名。

# 11. shutil.which(cmd)
# 类似linux的which命令，返回执行该命令的程序路径。Python3.3新增

# 12. shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
# 创建归档或压缩文件。

# 13. shutil.unpack_archive(filename[, extract_dir[, format]])
# 解压缩或解包源文件。
