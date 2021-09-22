import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)

class HVBoxLayoutExample(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")          # 创建一个 OK 按钮
        cancelButton = QPushButton("Cancel")  # 创建一个 Cancel 按钮

        hbox = QHBoxLayout()          # 新建一个水平布局
        hbox.addStretch(1)            # 给水平布局增加一个间隔元素，值设为 1
        hbox.addWidget(okButton)      # 给水平布局增加一个 OK 按钮
        hbox.addWidget(cancelButton)  # 给水平布局增加一个 cancel 按钮

        vbox = QVBoxLayout()          # 新建一个垂直布局
        vbox.addStretch(1)            # 给垂直布局增加一个间隔元素，值设为 1
        vbox.addLayout(hbox)          # 给垂直布局增加上面的水平布局

        self.setLayout(vbox)          # 把垂直布局加进界面内

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('框布局2')
        self.show()

app = QApplication(sys.argv)
ex = HVBoxLayoutExample()
app.exec_()