'''
master          默认开发分支
origin          默认远程版本库
index/stage     暂存区
workspace       工作区
repository      仓库区（或本地仓库）
remote          远程仓库


git常用命令速查表：

1、新建代码库
git init                                                # 在当前目录新建一个git代码仓库
git init [project_name]                                 # 新建一个目录，并将其初始化为git代码库
git clone <url>                                         # 下载一个项目和它整个代码历史

2、配置
git config --list                                       # 显示当前git的配置
git config -e [--global]                                # 编辑git配置文件
git config [--global] user.name '[your-name]'           # 提交代码的用户名
git config [--global] user.email '[your-email]'         # 提交代码的用户邮箱


3、增加/删除/修改文件
git status                                              # 查看状态
git diff                                                # 查看变更内容

git add [file1] [file2] ...                             # 添加指定文件到暂存区
git add [dir]                                           # 添加指定目录到暂存区（包括子目录）
git add .                                               # 添加当前目录的所有文件到暂存区

git add -p                                              # 添加每一个变化前，都要求确认，可以分多次提交

git rm [file1] [file2] ...                              # 删除工作区文件，并将此次删除放入到暂存区
git rm --cached [file]                                  # 停止追踪指定文件，但该文件会保留在工作区
git mv [file-original] [file-renamed]                   # 改名文件，并且将这次改名放入到暂存区

4、代码提交
git commit -m [message]                                 # 提交暂存区到仓库区
git commit [file1] [file2] ... -m [message]             # 提交暂存区的指定文件到仓库区

git commit -a                                           #
git commit -v                                           #

git commit --amend -m [message]                         # 重新提交
git commit --amend [file1] [file2] ...                  # 重新提交指定文件

5、分支
git branch                                              # 显示所有本地分支
git branch -r                                           # 列出所有远程分支
git branch -a                                           # 列出所有本地分支和远程分支
git branch [branch-name]                                # 新建一个分支，但依然停留在当前分支

git branch --track [branch] [remote-branch]             # 新建一个分支，并与指定的远程分支建立追踪关系
git branch -d [branch-name]                             # 删除分支
git push origin --delete [branch-name]                  # 删除远程分支
git branch -dr [remote/branch]                          # 删除远程分支
git checkout -b [branch]                                # 新建一个分支，并切换到该分支
git checkout -                                          # 切换到上一分支
git branch --set-upstream [branch] [remote-branch]      # 建立追踪关系，在现有分支与指定的远程分支之间

git merge [branch]                                      # 合并指定分支到当前分支
git rebase <branch>                                     # 衍合指定分支到当前分支
git cherry-pick [commit]                                # 选择一个commit，合并进当前分支

6、标签
git tag
git tag <tag-name>
git tag -d <tag-name>
git push origin :refs/tags/[tag-name]
git show [tag]
git push [remote] [tag]
git push [remote] --tags
git checkout -b [branch] [tag]

7、查看信息
git status
git log
git log --stat
git log -s [keyword]
git log [tag] HEAD --pretty=format:%s
git log [tag] HEAD --grep feature
git log --follow [file]
git whatchanged [file]
git log -p [file]
git log -5 --pretty --oneline
git shortlog -sn
git blame [file]
git diff
git diff --cached [file]
git diff HEAD
git diff [first-branch] ... [second-branch]
git diff --shortstat "@{03 爬虫基本原理 day ago}"
git show [commit]
git show --name-only [commit]
git show [commit]:[filename]
git reflog

8、远程操作
git fetch
git pull [remote] [branch]
git remote -v
git remote show [remote]
git remote add [shortname] [url]
git push [remote] [branch]
git push [remote] --force
git push [remote] --all
git push <remote> : <branch/tag-name>
git push --tags

9、撤销
git reset --hard HEAD
git checkout HEAD <file>
git revert <commit>
git log --before="1 days"
git checkout [file]
git checkout [commit] [file]
git checkout .
git reset [file]
git reset --hard
git reset [commit]
git reset --hard [commit]
git reset --keep [commit]
git revert [commit]
git stash
git stash pop

'''