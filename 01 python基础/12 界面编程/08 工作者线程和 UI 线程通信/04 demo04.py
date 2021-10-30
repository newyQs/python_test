import sys
import time
import threading
from PyQt5.Qt import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox


class FourExample(QWidget):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.sinOut.connect(self.outResult)
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('等待结果中...', self)
        self.btn = QPushButton('开始', self)

        self.lbl.move(100, 100)
        self.btn.move(100, 150)

        self.btn.clicked.connect(self.startCompute)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('阻塞耗时例子4')
        self.show()

    def outResult(self, rst):  # 在主线程（UI 线程）中操作 UI
        self.lbl.setText(rst)
        QMessageBox.information(None, "工作者线程", "老鸟python")

    def startCompute(self):
        t = threading.Thread(target=self.func)
        t.start()

    def func(self):  # 工作者线程做运算
        time.sleep(10)
        self.sinOut.emit("任务完成")  # 把结果投递到消息队列


app = QApplication(sys.argv)
ex = FourExample()
app.exec_()
