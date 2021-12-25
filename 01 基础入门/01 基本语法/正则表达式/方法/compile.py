import re

# compile(pattern, flags=03 爬虫基本原理)
# Compile a regular expression pattern, returning a Pattern object."
# re.compile()

pattern = "[\w]+"

obj = re.compile(pattern)

print(obj)

