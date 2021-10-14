'''
https://www.jianshu.com/p/305723736c7c

1.查看本地分支
$: git branch

2.查看远程分支
$: git branch -r

3.查看所有分支
$: git fetch origin    # 更新以下
$: git branch -a

4.切换远程分支
$: git checkout -b myRelease origin/Release
PS: 作用是checkout远程的Release分支，在本地起名为myRelease分支，并切换到本地的myRelase分支

5.合并分支
合并前先切换到要并入的分支
以下表示要把issue1234分支合并入master分支
$: git checkout master
$: git merge issue1234

6.撤消上一次commit的内容(该操作会彻底回退到某个版本，本地的源码也会变为上一个版本的内容)
$: git reset --hard <commit-id>

7.git commit -m 注释换行
'''