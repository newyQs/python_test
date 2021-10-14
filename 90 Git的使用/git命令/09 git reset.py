'''
https://www.jianshu.com/p/c2ec5f06cf1a

git reset 命令
有时候，我们用Git的时候有可能commit提交代码后，发现这一次commit的内容是有错误的，那么有两种处理方法：
1。修改错误内容，再次commit一次
2。使用git reset 命令撤销这一次错误的commit
第一种方法比较直接，但会多次一次commit记录。

意思就是可以让HEAD这个指针指向其他的地方。
例如我们有一次commit不是不是很满意，需要回到上一次的Commit里面。
那么这个时候就需要通过reset，把HEAD指针指向上一次的commit的点。

作用：用于回退版本，可以指定退回某一次提交的版本
语法：git reset [--soft | --mixed | --hard] [HEAD]

参数说明：
    --mixed为默认，可以不带该参数。
    用于重置暂存区的文件与上一次的提交(commit)保持一致，工作区文件内容保持不变。
实例：
    git reset HEAD                  #
    git reset HEAD^                 # 回退到所有内容到上一版本
    git reset HEAD^ hello.py        # 回退hello.py文件的版本到上一版本
    git reset 052e                  # 回退到指定版本

    --soft 回退到某个版本
实例：
    git reset --soft HEAD~3         # 回退上上上一个版本

    --hard 撤销工作区中所有未提交的修改内容，将暂存区与工作区都回到上一次版本，并删除之前的所有信息提交

实例：
    git reset –hard HEAD~3          # 回退上上上一个版本
    git reset –hard bae128          # 回退到某个版本回退点之前的所有信息。
    git reset --hard origin/master  # 将本地的状态回退到和远程的一样

注意：谨慎使用 –hard 参数，它会删除回退点之前的所有信息。

HEAD说明：
    HEAD 表示当前版本
    HEAD^ 上一个版本
    HEAD^^ 上上一个版本
    HEAD^^^ 上上上一个版本
以此类推...
    可以使用 ～数字表示
    HEAD~0 表示当前版本
    HEAD~1 上一个版本
    HEAD^2 上上一个版本
    HEAD^3 上上一个版本
以此类推...

git reset HEAD
    命令用于取消已缓存的内容。也就是取消git add命令中提交到暂存区的内容

问题：
    git reset 命令中的参数
'''