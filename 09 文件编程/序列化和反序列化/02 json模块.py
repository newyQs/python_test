import json

'''
对于其他编程语言，需要使用json模块来提供序列化
经过json序列化后，都会变成字符类型
'''
# 原始数据
data = [1, True, ("hello", None)]

# 1.dumps和loads
json_data = json.dumps(data)
print(type(json_data))  # json序列化后都是字符流

with open('./io/json.txt', 'w') as f:
    f.write(json_data)

with open('./io/json.txt', 'r') as f:
    info = f.read()

print(info, type(info))

# 2.dump和load
with open('./io/jd.txt', 'w') as f:
    json_data = json.dump(data, f)

with open('./io/jd.txt', 'r') as f:
    msg = json.load(f)

print(msg, type(msg))

# 3.json模块支持序列化数据类型的局限性
# 3.1 python中set类型不支持
s = {1, 2, 3}
ss = json.dumps(s)  # TypeError: Object of type set is not JSON serializable

# 3.2 python的元组会转换成list类型
t = (1, 2, 3)
tt = json.dumps(t)
ts = json.loads(tt)
print(ts)  # list

# 3.3 dict支持键为字符串类型，对于其他基本类型则会强转成字符串类型，如果是tuple则会报错
seqdata = json.dumps({1: 1, 1.1: 2, "a": 3, None: 4, True: 5})
dd = json.loads(seqdata)
print(dd)

# 3.4 序列化字典的键必须是str,int,float,bool,None
seqdata = json.dumps({(1, 2): 1})  # TypeError: keys must be str, int, float, bool or None, not tuple

# 4.通用类型序列化
'''
python数据类型：
    int <==> int：整形
    float <==> float：浮点型
    list/tuple <==> []:数组
    dict <==> {}：序列化时，dict的键必须是字符串
    str/unicode <==> unicode：
    bool <==> bool :序列化时将True/False变成字符流，反序列化时，变回True/False
    None <==> null :序列化时将None变成null字符流，反序列化时，变回None
    set 不支持
'''

# 5.自定义类型的序列化
#

