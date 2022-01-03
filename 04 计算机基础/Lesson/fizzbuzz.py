"""

"""


class FizzBuzz:
    
    @staticmethod
    def of(number):
        result = ''
        if number == 0:
            raise Exception('不能为0')
        if number % 3 == 0:
            result += 'Fizz'
        if number % 5 == 0:
            result += 'Buzz'

        return str(number) if result == '' else result
