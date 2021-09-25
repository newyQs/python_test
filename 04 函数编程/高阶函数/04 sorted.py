# {}
d = {'chinese': 89, 'math': 98, 'englise': 82}

# print(d.keys())  # dict_keys(['chinese', 'math', 'englise'])
# print(d.values())  # dict_values([89, 98, 82])
# print(d.items())  # [('englise', 82), ('chinese', 89), ('math', 98)]
print(sorted(d.items(), key=lambda x: x[1]))

# [{},{},{}]
dd = [{'name': 'lee', 'age': 28}, {'name': 'jack', 'age': 32}, {'name': 'lucy', 'age': 24}]
print(sorted(dd, key=lambda x: x['age']))
