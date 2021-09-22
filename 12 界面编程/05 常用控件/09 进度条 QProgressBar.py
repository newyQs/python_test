import sys
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)


class ProgressBarExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 500, 25)

        self.btn = QPushButton('开始', self)
        self.btn.move(30, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('进度条')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('结束')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            self.timer.start(100, self)
            self.btn.setText('停止')


app = QApplication(sys.argv)
ex = ProgressBarExample()
app.exec_()
