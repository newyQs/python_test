from multiprocessing.sharedctypes import typecode_to_type

print(typecode_to_type)

"""
{
    'c': <class 'ctypes.c_char'>, 
    'u': <class 'ctypes.c_wchar'>, 
    'b': <class 'ctypes.c_byte'>, 
    'B': <class 'ctypes.c_ubyte'>, 
    'h': <class 'ctypes.c_short'>, 
    'H': <class 'ctypes.c_ushort'>, 
    'i': <class 'ctypes.c_long'>, 
    'I': <class 'ctypes.c_ulong'>, 
    'l': <class 'ctypes.c_long'>, 
    'L': <class 'ctypes.c_ulong'>, 
    'q': <class 'ctypes.c_longlong'>, 
    'Q': <class 'ctypes.c_ulonglong'>, 
    'f': <class 'ctypes.c_float'>, 
    'd': <class 'ctypes.c_double'>
}
"""
