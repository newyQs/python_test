n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

# while...else
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:  # 当条件不在满足时
    print(count, " 大于或等于 5")
