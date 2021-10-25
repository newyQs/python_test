#!bin/bash

# 单引号
str='this is a string'

# 双引号
your_name="runoob"
str="Hello, I know you are \"$your_name\"! \n"

# 拼接字符串
echo "hello $your_name"

greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1

greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3

# 获取字符串长度
string="abcd"
echo ${#string} 

# 截取字符串子串
strings="runoob is a great site"
echo ${strings:1:4}

# 查找子字符串
string="runoob is a great site"
echo `expr index "$string" io`
