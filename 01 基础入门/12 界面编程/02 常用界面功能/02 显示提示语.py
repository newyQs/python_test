import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class TooltipWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用 10px 滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 当鼠标停留在该窗口内时，会弹出一个提示语
        self.setToolTip('这是 <b>python</b> 的 widget')

        # 创建一个 PushButton，当鼠标停留在该按钮上时，会弹出一个提示语
        btn = QPushButton('jack', self)
        btn.setToolTip('这是 <b>python</b> 的 button')

        # btn.sizeHint 显示默认尺寸
        btn.resize(btn.sizeHint())

        # 移动窗口的位置
        btn.move(50, 50)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('提示语')
        self.show()


app = QApplication(sys.argv)
ex = TooltipWidget()
app.exec_()
