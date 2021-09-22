import re

'''
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'Pattern', 
'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', 
'__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
'__version__', '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pickle', '_special_chars_map', 
'_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 
'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
'''
# 修饰符：A/I/L/M/S/T/U/X
# 常用：I=>对大小写不敏感；M=>做多行匹配；

# 方法：match/search/compile/findall/finditer/splite/sub/subn
# 1 re.match(pattern, string, flags=0)

# 2 re.search(pattern, string, flags=0)

# 3 re.sub(pattern, repl, string, count=0, flags=0)

#

