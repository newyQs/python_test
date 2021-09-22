import random

'''
'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 
'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 
'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'
'''
# randint/random/randrange/sample/shuffle/uniform

# 1.random():用于生成一个0~1之间的随机浮点数==> [0,1)
# print(random.random())

# 2.uniform(a,b):用于生成一个a~b之间的随机浮点数==> [a,b]
# print(random.uniform(2, 5))

# 3.randint(a,b):用于生成一个a~b之间的随机整数==> [a,b]
# print(random.randint(3, 7))

# 4.randrange(a, b, step):在指定范围内[a,b]并指定间隔step返回一个数
# print(random.randrange(2, 12, 2))

# 5.choice(sequence)：从一个序列中，随机返回一个值
# print(random.choice([2, 3, 12, 24, 32, 4, 5, 6]))

# 6.random.shuffle(x[, random])：将已有的列表打乱，改变原列表，返回值为None
p = ['A', 'B', 'C', 'D', 'E']
random.shuffle(p)
print(p)

# 7.random.sample(sequence, k):从指定序列中获取指定长度的序列并随机排序，不会修改原有序列
s = random.sample([1, 2, 3, 4], 2)
print(s)
