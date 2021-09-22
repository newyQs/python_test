from multiprocessing import Process, Array


def func(data, share_data):
    share_data[0] = data
    print(f'子进程中share_data的值是：{share_data[0]}')


if __name__ == '__main__':
    '''
    对于 Array 数组类，括号内的“i”表示它内部的元素全部是 int 类型，数组内的元素可以预先指定，也可以只指定数组的长度
    Array 类在实例化的时候必须指定数组的数据类型和数组的大小，比如我们指定 3 个整数，可以写成 shareddatas= Array("i", 3)
    对于数据类型有下面的对应关系：
    'c': ctypes.c_char, 'u': ctypes.c_wchar,
    'b': ctypes.c_byte, 'B': ctypes.c_ubyte,
    'h': ctypes.c_short, 'H': ctypes.c_ushort,
    'i': ctypes.c_int, 'I': ctypes.c_uint,
    'l': ctypes.c_long, 'L': ctypes.c_ulong,
    'f': ctypes.c_float, 'd': ctypes.c_double
    '''
    share_data = Array('i', 1)
    # print(share_data)
    p = Process(target=func, args=(120, share_data))
    p.start()
    p.join()

    print(f'主进程share_data的值是：{share_data[0]}')
