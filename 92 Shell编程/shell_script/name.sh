#!bin/bash

# 字符串
name1=jack
name2='lucy'
name3="tom"

# 使用变量
echo $name1 $name2 ${name3}

# 重新赋值
name3="xiaoming"
echo $name3

# 只读变量
#readonly myurl="https://www.baidu.com"
#myurl="http://sougou.com"
#echo $myurl

# 删除变量,不能删除只读变量
unset name2
echo $name2
