import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox


class ThreeExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('等待结果中...', self)
        self.btn = QPushButton('开始', self)

        self.lbl.move(100, 100)
        self.btn.move(100, 150)

        self.btn.clicked.connect(self.startCompute)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('阻塞耗时例子3')
        self.show()

    def startCompute(self):
        t = threading.Thread(target=self.func)
        t.start()

    def func(self):  # 工作者线程启动的函数
        time.sleep(10)
        QMessageBox.information(None, "工作者线程", "老鸟python")  # 非 UI 线程中创建资源


app = QApplication(sys.argv)
ex = ThreeExample()
app.exec_()
