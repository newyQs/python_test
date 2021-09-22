class Temperature:
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def fahrenheit(self):  # Getter should be return or yield something
        self.temperature = self.temperature * 1.8 + 32


temp = Temperature(20)
temp.fahrenheit
print(temp.temperature)
'''
当使用属性装饰器的时候，应该确保有返回值，在类/方法中调用属性装饰器返回值会更加容易
'''