import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit


class SignalsSlotsTwo(QWidget):
    sinOut = pyqtSignal(str)  # 定义一个消息对象

    def __init__(self):
        super().__init__()
        self.sinOut.connect(self.outText)  # 关联槽函数 outText
        self.initUI()

    def initUI(self):
        self.edit = QLineEdit("编辑框", self)  # 定义一个编辑框控件
        self.edit.move(100, 100)  # 移动编辑框到窗口坐标（100, 100）

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('信号槽演示2')
        self.show()

        self.sinOut.emit("老鸟python")  # 往消息队列里面投递消息（发信号）

    def outText(self, text):  # 槽函数
        self.edit.setText(text)


app = QApplication(sys.argv)
ex = SignalsSlotsTwo()
app.exec_()
