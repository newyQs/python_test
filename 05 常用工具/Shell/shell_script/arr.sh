#!bin/bash

# 仅仅支持一维数组
arr1=(11 12 13 14)
arr2=(
 4
 5
 "jack"
 2.5
)
arr3[0]=1
arr3[1]=4
arr3[5]=12
arr3[12]=24

# 读取数组
echo ${arr1[1]} 
echo ${arr2[0]} 
echo ${arr3[3]}

# 读取数组全部元素
echo "数组arr1：${arr1[*]}"
echo "数组arr2：${arr2[@]}"

# 获取数组长度
echo "数组长度：${#arr3[*]}"

# 删除数组元素
echo "元素删除前：${arr1[0]}"
unset arr1[0]
echo "元素删除后：${arr1[0]}"

# 删除数组
unset arr3
echo "删除数组后：${arr3[*]}，长度：${#arr3[*]}"

# 遍历数组元素
for item in ${arr1[*]}; do
	echo "item:${item}"
done

arr=(1 2 3 4 5) # 注意是用空格分开，不是逗号！！
for i in "${!arr[@]}"; do 
    printf "%s\t%s\n" "$i" "${arr[$i]}"
done
