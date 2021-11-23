import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox


class SignalsSlotsOne(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("老鸟button", self)  # 定义一个按钮控件
        self.btn.move(100, 100)  # 移动按钮到窗口坐标（100, 100）

        self.btn.clicked.connect(self.buttonClicked)  # 给 clicked 消息关联消息处理函数

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('信号槽演示1')
        self.show()

    def buttonClicked(self):  # 槽函数
        QMessageBox.information(None, "弹框", self.btn.text())


app = QApplication(sys.argv)
ex = SignalsSlotsOne()
app.exec_()
