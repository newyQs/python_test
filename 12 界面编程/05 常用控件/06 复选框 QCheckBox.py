import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class CheckBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('显示标题', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('选中复选框')
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('选中复选框')
        else:
            self.setWindowTitle('未选中复选框')


app = QApplication(sys.argv)
ex = CheckBoxExample()
app.exec_()
