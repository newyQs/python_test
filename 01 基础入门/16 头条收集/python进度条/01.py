"""

"""
import sys
import time

for i in range(1, 101):
    print("\r", end="")
    print("进度: {}%: ".format(i), "▓" * (i // 2), end="")
    sys.stdout.flush()
    time.sleep(0.05)
