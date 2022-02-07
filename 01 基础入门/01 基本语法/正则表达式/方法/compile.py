import re

# compile(pattern, flags=0)
# Compile a regular expression pattern, returning a Pattern object."
# re.compile()

pattern = "[\w]+"

obj = re.compile(pattern)

print(obj)  # re.compile('[\\w]+')
print(type(obj))  # <class 're.Pattern'>
