import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)
from PyQt5.QtCore import QSize

class PixmapExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap("birdpython.png")  # 确保当前目录下有该图片
        btn = QPushButton(self)
        btn.setIcon(QIcon(pixmap))  # 需要用 QIcon 转换一下
        btn.setGeometry(100, 200, 100, 50)  # 设置按钮显示位置和大小
        btn.setIconSize(QSize(100, 50))  # 设置按钮上的图片大小

        self.setWindowTitle('画布')
        self.setGeometry(600, 200, 800, 500)
        self.show()

app = QApplication(sys.argv)
ex = PixmapExample()
app.exec_()