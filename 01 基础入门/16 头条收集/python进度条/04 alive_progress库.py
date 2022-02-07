"""
https://pypi.org/project/alive-progress/#description
"""
import time
from alive_progress import alive_bar

# 假设需要执行100个任务
with alive_bar(len(range(100))) as bar:
    for item in range(100):  # 遍历任务
        bar()  # 显示进度
        """代码"""
        # 假设这代码部分需要0.05s
        time.sleep(0.05)
