import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QApplication)


class HBoxLayoutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")  # 创建一个 OK 按钮
        cancelButton = QPushButton("Cancel")  # 创建一个 Cancel 按钮

        hbox = QHBoxLayout()  # 创建一个水平布局

        hbox.addStretch(1)  # 给水平布局增加一个间隔元素，值设为 1
        hbox.addWidget(okButton)  # 给水平布局增加一个 ok 按钮
        hbox.addWidget(cancelButton)  # 给水平布局增加一个 cancel 按钮

        self.setLayout(hbox)  # 给界面加入水平布局

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('框布局')
        self.show()


app = QApplication(sys.argv)
ex = HBoxLayoutExample()
app.exec_()
