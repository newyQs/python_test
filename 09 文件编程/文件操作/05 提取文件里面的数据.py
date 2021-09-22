import csv

filename = './collect.txt'

with open(filename, 'r') as f:
    data_list = f.readlines()

for item in data_list:
    item_list = item.split(';')
    for value in item_list:
        value_list = value.split('=')
        if len(value_list) > 1:
            info = value_list[1]  # 需要的数据
            print(info)
            with open('./data.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(info)
