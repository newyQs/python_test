"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""
import time


class DateUtils:

    @classmethod
    def de_date_time(cls):
        # result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # -> 2022-01-02 19:13:55
        result = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())  # -> Sun Jan 02 19:22:22 2022
        return result

    @classmethod
    def en_date_time(cls, a):
        result = time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S"))
        return result


du = DateUtils()
if __name__ == '__main__':
    print(du.de_date_time())
    print(du.en_date_time("2022-01-02 19:13:55"))
