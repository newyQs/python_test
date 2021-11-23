import csv

data = []
sum_data = 0

with open('./numbers.csv', 'r', encoding='utf-8') as f:
    data.extend(list(csv.reader(f)))
print(data)
for row in data[1:]:
    sum_data += sum(map(int, row))

print(sum_data)

