import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication)


class LineEditExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('编辑框')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


app = QApplication(sys.argv)
ex = LineEditExample()
app.exec_()
