"""
https://pypi.org/project/tqdm/#description
"""
import time
from tqdm import tqdm

for i in tqdm(range(1, 60)):
    """
    代码
    """
    # 假设这代码部分需要0.05s，循环执行60次
    time.sleep(0.05)
