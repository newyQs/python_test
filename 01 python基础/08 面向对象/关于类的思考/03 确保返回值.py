class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def fahrenheit(self):
        return self.temperature * 1.8 + 21


temp = Temperature(22)
temp.fahrenheit()

print(temp.temperature)
