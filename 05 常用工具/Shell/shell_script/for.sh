#!bin/bash

for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done

# 
for str in This is a string
do
    echo $str
done

#
for i in {1..100}
do
    echo $i
done

for i in `seq 1 100`
do
    echo $i
done

for ((i=1; i<=100; i ++))
do
	echo $i
done

