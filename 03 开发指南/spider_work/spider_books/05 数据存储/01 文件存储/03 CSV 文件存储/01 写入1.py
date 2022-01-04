"""

"""
import csv

with open('data.csv', 'w') as csvfile:
    # writer = csv.writer(csvfile)
    # 如果想修改列与列之间的分隔符，可以传入 delimiter 参数
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
