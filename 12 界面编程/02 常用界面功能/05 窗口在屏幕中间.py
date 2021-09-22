import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class CenterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 500)
        self.center()
        self.setWindowTitle('居中窗口')
        self.show()

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())


app = QApplication(sys.argv)
ex = CenterWidget()
app.exec_()
