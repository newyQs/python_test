import csv

sum_data = 0

with open('./numbers.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in list(reader)[1:]:
        sum_data += sum(map(int, row))

print(sum_data)
