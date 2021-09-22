import re

data = ['abc0', 'abc9', 'abc5', 'cba2']

convert = lambda text: float(text) if text.isdigit() else text
alphaum = lambda key: [convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]*)', key)]

data.sort(key=alphaum)
