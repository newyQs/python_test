#!bin/bash

arr=(1 2 3 4 5) # 注意是用空格分开，不是逗号！！

${#array[@]}

# 遍历（For循环法）：
for var in ${arr[@]};
do
    echo $var
done

# 遍历（带数组下标）：
for i in "${!arr[@]}";
do
    printf "%s\t%s\n" "$i" "${arr[$i]}"
done

# 遍历（While循环法）：
i=0
while [ $i -lt ${#array[@]} ]
do
    echo ${array[$i]}
    let i++
done

# 遍历（for循环次数）
for i in {1..5}
do
   echo "Welcome $i times"
done
