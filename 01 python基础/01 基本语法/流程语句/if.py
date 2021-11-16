"""
操作符：

类型	    False	                    True
布尔	False(与0等价)	            True(与1等价)
数值	0,   0.0	                非零的数值
字符串	'',  ""(空字符串)	        非空字符串
容器	[],  (),  {},  set()	至少有一个元素的容器对象
None	    None	                非None对象

"""
var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

################################################
var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

################################################
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

input("点击 enter 键退出")

################################################
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")
