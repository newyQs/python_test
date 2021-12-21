"""
https://mp.weixin.qq.com/s?src=11&timestamp=1640097094&ver=3510&signature=I1pIMcd0V8aguE2*tl0tikU-qXGboitsHCI*oFZ4TAcqj0-2U1X6aMS8yhxM-6ilohg0rFuq6LUlKLWoefFe9c8mP69FzARcJGJYd98nPDqmyOevODatpIqWwiZEuPlF&new=1
异步、并发、协程、Future

1.同步函数和异步函数的写法；
2.异步函数的调用；
3.
"""


def regular_double(x):
    return 2 * x


async def async_double(x):
    return 2 * x
