'''
1.变量命名规范
 1.命名只能使用英文字母，数字，下划线，首个字符不能以数字开头；
 2.中间不能有空格，可以使用下划线；
 3.不能使用标点符号；
 4.不能使用bash里面的关键字;
 注意：变量名与等号之间不能有空格。

for file in `ls /etc`
或
for file in $(ls /etc)

以上语句可以将/etc下目录的文件名循环出来

2.使用变量
your_name="lqs"
echo $our_name
echo ${your_name}

# 加{}可以帮助解释器识别变量的边界：
for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done

# 已定义的变量，可以被重新定义：
your_name="tom"
echo $your_name
your_name="alibaba"
echo $your_name
# 第二次赋值的时候不能写$your_name="alibaba"，使用变量的时候才加美元符（$）

# 只读变量：
#!/bin/bash
myUrl="https://www.google.com"
readonly myUrl
myUrl="https://www.runoob.com"
# 只读变量的值不能被改变

# 删除变量：
unset variable_name
# 变量被删除后不能再次使用。unset 命令不能删除只读变量

3.变量类型
 1.局部变量 局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量;
 2.环境变量 所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量;
 3.shell变量 shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行;

4.字符串
# 可以用单引号，也可以用双引号，也可以不加引号

# 单引号：
str='this is a string'
# 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
# 单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用；

# 双引号：
your_name="runoob"
str="Hello, I know you are \"$your_name\"! \n"
echo -e $str
# 双引号里可以有变量
# 双引号里可以出现转义字符

# 拼接字符串：
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1
# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3

# 获取字符串长度
string="abcd"
echo ${#string} #输出 4

# 提取子字符串：从字符串第 2 个字符开始截取 4 个字符
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo

# 查找子字符串：查找字符 i 或 o 的位置(哪个字母先出现就计算哪个)
string="runoob is a great site"
echo `expr index "$string" io`  # 输出 4

5.数组
# bash支持一维数组（不支持多维数组），并且没有限定数组的大小

# 定义数组
数组名=(值1 值2 ... 值n)

# 如
array_name=(value0 value1 value2 value3)
# 或者
array_name=(
    value0
    value1
    value2
    value3
)
# 还可以单独定义数组的各个分量：
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen

# 读取数组
${数组名[下标]}
valuen=${array_name[n]}

# 获取数组中的所有元素
echo ${array_name[@]}
echo ${array_name[*]}

# 获取数组的长度
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
'''