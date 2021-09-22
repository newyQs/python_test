class MutiplyByTwo:
    def __init__(self, number, limit):
        self.number = number
        self.counter = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        value = self.counter * self.number
        if value > self.limit:
            raise StopIteration
        else:
            return value


# for循环能够捕捉StopIteration异常并作处理
for num in MutiplyByTwo(500, 100000):
    print(num)
