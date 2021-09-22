import sys
import threading
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QApplication


class SignalsSlotsFive(QWidget):
    sinOut = pyqtSignal()  # 定义一个消息对象

    def __init__(self):
        super().__init__()
        self.sinOut.connect(self.outText, Qt.DirectConnection)  # 不同线程默认是异步的，在此改成同步

    def outText(self):  # 槽函数
        print("消息处理完毕")


def run():  # 消息投递函数
    ex.sinOut.emit()
    print("消息投递过了")  # 该语句后于槽函数执行


app = QApplication(sys.argv)
ex = SignalsSlotsFive()
t = threading.Thread(target=run)
t.start()
app.exec_()
