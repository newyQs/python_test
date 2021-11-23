'''
同线程中，通过给 connect 函数设置 Qt.QueuedConnection 参数，可以使消息投递函数和消息处理函数变为异步
'''
import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QApplication


class SignalsSlotsThree(QWidget):
    sinOut = pyqtSignal()  # 定义一个消息对象

    def __init__(self):
        super().__init__()
        self.sinOut.connect(self.outText, Qt.QueuedConnection)  # 同线程默认是同步的，在此改成异步
        self.init()

    def init(self):
        self.sinOut.emit()  # 往消息队列里面投递消息（发信号）
        print("消息投递过了")  # 该语句先于槽函数执行

    def outText(self):  # 槽函数
        print("消息处理完毕")


app = QApplication(sys.argv)
ex = SignalsSlotsThree()
app.exec_()
