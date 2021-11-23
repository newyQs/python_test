import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class IconWidget(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类 QWidget 的构造函数
        self.initUI()  # 界面绘制交给 InitUi 方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(600, 200, 800, 500)

        # 设置窗口的标题
        self.setWindowTitle('图标')

        # 设置窗口的图标，确保当前目录下有 cat.png 图片
        self.setWindowIcon(QIcon('cat.png'))

        # 显示窗口
        self.show()


app = QApplication(sys.argv)  # 创建应用程序
ex = IconWidget()  # 创建窗口对象
app.exec_()  # 进入消息循环
