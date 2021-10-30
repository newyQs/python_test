import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class OneExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('等待结果中...', self)
        self.btn = QPushButton('开始', self)

        self.lbl.move(100, 100)
        self.btn.move(100, 150)

        self.btn.clicked.connect(self.startCount)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('阻塞耗时例子1')
        self.show()

    def startCount(self):
        time.sleep(10)  # 模拟处理行为需要 10 秒钟
        self.lbl.setText("任务完成")


app = QApplication(sys.argv)
ex = OneExample()
app.exec_()
