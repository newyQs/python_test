import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QApplication)


class SplitterExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)  # 布局控件
        topleft = QFrame(self)  # 左边的边框
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)  # 右边的边框
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)  # 底端的边框
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)  # 分割器 1
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)  # 分割器 2
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('QSplitter')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


app = QApplication(sys.argv)
ex = SplitterExample()
app.exec_()
