import re

# sub(pattern, repl, string, count=0, flags=0)
# Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl.
# re.sub(pattern, repl, string, count=0, flags=0)

# subn(pattern, repl, string, count=0, flags=0)
# return a 2-tuple containing (new_string, number).
# re.subn(pattern, repl, string, count=0, flags=0)

pattern = "[\w]+"

print(re.sub("\d+", "222", "hello 123 world 456"))
print(re.subn("\d+", "222", "hello 123 world 456"))

s = "hello 123 world 456"
print(s.replace("123", "222"))
