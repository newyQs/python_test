class MutiplyByTwo:
    def __init__(self, number):
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.counter * self.number


for num in MutiplyByTwo(500):
    print(num)
