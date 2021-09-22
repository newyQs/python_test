def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


for x in [-1, 0, 1]:
    print(sign(x))


# Prints "negative", "zero", "positive"

def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)


hello('Bob')  # Prints "Hello, Bob"
hello('Fred', loud=True)  # Prints "HELLO, FRED!"
