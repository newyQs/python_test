import os

'''
['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 
'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 
'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 
'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', 
'_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 
'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 
'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 
'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 
'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 
'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 
'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 
'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 
'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 
'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size',
'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
'''
# 1.目录的增删改查
# print(os.listdir('.'))  # 列举指定目录下所有的文件（.表示当前目录）

# os.mkdir('./04 collections')  # 创建一个空目录

# os.rmdir('./04 collections') # 删除一个空目录。注意：无法删除非空目录

# os.makedirs('./test1/test2')  # 创建多层递归目录。注意：如果目录全部存在则创建失败

# os.removedirs('./test1/test2')  # 删除多层递归目录。注意：目录中有文件则无法删除

# os.chdir('e:/code')  # 切换到指定目录下
# print(os.listdir('.'))

# os.rename(src_filename, dest_filename) # 修改目录或文件名

# 2.判断：返回True或者False
# os.path.exists(path)  # 判断文件或目录是否存在，存在返回True，否则返回False
# os.path.isfile(path)  # 判断是否是文件
# os.path.isdir(path)  # 判断是否是目录

# 3.系统操作
# print(os.sep) # 获取系统的分隔符,windows返回\，Linux系统返回/

# print(os.name)  # 获取使用的平台，windows返回nt,linux/Unix返回posix

# print(os.getcwd()) # 获取当前的全路径

# print(os.getenv('path')) # 获取环境变量

# 4.path模块
# print(os.path.basename('e:/code/lnodes/setupppp.py')) # 返回文件名。注意：不要求路径正确或文件名存在

# print(os.path.dirname('e:/code/lnodes/setupppp.py')) # 返回文件路径。注意：不要求路径正确或文件名存在

# print(os.path.getsize('e:/code/lnodes/setup.py'))  # 获取文件大小。注意：路径必须正确，文件存在

# print(os.path.abspath('e:/code/lnodes/setup.py'))  # 获取绝对路径

# print(os.path.join('c:/user', '04 collections.py'))  # 拼接路径
