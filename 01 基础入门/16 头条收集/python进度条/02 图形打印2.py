"""

"""
import time

t = 60
print("**************带时间的进度条**************")
start = time.perf_counter()
for i in range(t + 1):
    finsh = "▓" * i
    need_do = "-" * (t - i)
    progress = (i / t) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")
    time.sleep(0.05)
