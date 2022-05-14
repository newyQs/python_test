1. 多人开发合并冲突

feat-test  (目标分支)   feat-test-lqs  (个人开发分支)

情况1：

在个人分支下：
```
git stash
git checkout feat-test
git pull
git checkout feat-test-lqs
git merge feat-test    
git stash pop   		==>   有冲突
手动修改冲突
git add .
git commit -m 'stash merge'
git push origin feat-test-lqs
```

情况2：这种会多很多提交记录

feat-test-lqs  (个人开发分支)
 
在该分支下：
```
git add . 
git commit -m 'dsds'
git checkout  feat-test
git pull
git checkout  feat-test-lqs
git merge  feat-test  ==> 提示有冲突
手动修改冲突
git add .
git commit -m 'ds'
git push origin feat-test-lqs
```

情况3：有提交有保存
```
修改了一些代码
  git add .
  git commit -m 'dsds'

  修改了一些代码
  git stash   		 ==>恢复到最近一次提交，即dsds
  git checkout feat-test
  git pull  			 ==>拉取最新代码

  git checkout feat-test-lqs         
  git merge feat-test       	  ==> 有冲突
  手动修改冲突
  git add .
  git commi - m 'merge'
  git stash pop  		 ==> 有冲突
  手动改冲突
  git add .
  git commit -m 'stash pop'
  git push origin feat-test-lqs
```

## 知识点：

方法一、stash
```
1 git stash
2 git commit
3 git stash pop

git stash: 备份当前的工作区的内容，从最近的一次提交中读取相关内容，让工作区保证和上次提交的内容一致。同时，将当前的工作区内容保存到Git栈中。
git stash pop: 从Git栈中读取最近一次保存的内容，恢复工作区的相关内容。由于可能存在多个Stash的内容，所以用栈来管理，pop会从最近的一个stash中读取内容并恢复。
git stash list: 显示Git栈内的所有备份，可以利用这个列表来决定从那个地方恢复。
git stash clear: 清空Git栈。此时使用gitg等图形化工具会发现，原来stash的哪些节点都消失了。
```

方法二、放弃本地修改，直接覆盖
```
1 git reset --hard
2 git pull

回退命令：
git reset --hard HEAD^ 回退到上个版本
git reset --hard HEAD~3 回退到前3次提交之前，以此类推，回退到n次提交之前
git reset --hard commit_id 退到/进到，指定commit的哈希码（这次提交之前或之后的提交都会回滚）
```