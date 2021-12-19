"""
https://pypi.org/project/progressbar/#description
"""
import time
import progressbar

p = progressbar.ProgressBar()
# # 假设需要执行100个任务，放到ProgressBar()中
for i in p(range(100)):
    """
    代码
    """
    # 假设这代码部分需要0.05s
    time.sleep(0.05)
