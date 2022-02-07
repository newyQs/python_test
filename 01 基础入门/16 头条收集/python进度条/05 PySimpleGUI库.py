"""
PySimpleGUI也是一种动态进度条库，该库是自带GUI界面（基于PyQt，Tkinter等）
https://pypi.org/project/PySimpleGUI/#description
"""
import time
import PySimpleGUI as sg

count = range(100)
for i, item in enumerate(count):
    sg.one_line_progress_meter('实时进度条', i + 1, len(count), '-key-')
    """代码"""
    # 假设这代码部分需要0.05s
    time.sleep(0.05)
