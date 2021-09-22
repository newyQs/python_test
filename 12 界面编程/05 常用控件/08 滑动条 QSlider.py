import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)


class SliderExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)  # 设置滚动条的位置和大小
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setText("0")
        self.label.move(80, 20)  # 设置 label 的位置

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('滑动条')
        self.show()

    def changeValue(self, value):
        self.label.setText(str(value))


app = QApplication(sys.argv)
ex = SliderExample()
app.exec_()
