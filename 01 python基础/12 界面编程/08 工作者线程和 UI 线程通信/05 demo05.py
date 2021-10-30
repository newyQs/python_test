import sys
import time
from PyQt5.Qt import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox


class FiveExample(QWidget):
    sinOut = pyqtSignal(str)  # 创建一个消息对象

    def __init__(self):
        super().__init__()
        self.workthd = Workthread(self.sinOut)  # 创建一个线程对象
        self.sinOut.connect(self.outResult)  # 给消息对象关联槽函数
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('等待结果中...', self)
        self.btn = QPushButton('开始', self)

        self.lbl.move(100, 100)
        self.btn.move(100, 150)

        self.btn.clicked.connect(self.startCompute)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('阻塞耗时例子5')
        self.show()

    def outResult(self, rst):  # 在主线程（UI 线程）中操作 UI
        self.lbl.setText(rst)
        QMessageBox.information(None, "工作者线程", "老鸟python")

    def startCompute(self):
        self.workthd.start()  # 启动工作者线程


class Workthread(QThread):
    def __init__(self, sinOut):
        super(Workthread, self).__init__()
        self.sinOut = sinOut

    def run(self):  # 工作者线程做任务
        time.sleep(10)
        self.sinOut.emit("任务完成")


app = QApplication(sys.argv)
ex = FiveExample()
app.exec_()
