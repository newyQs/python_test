import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)


class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("老鸟python", self)

        combo = QComboBox(self)
        combo.addItem("python3教程")
        combo.addItem("设计模式教程")
        combo.addItem("Django教程")
        combo.addItem("爬虫教程")
        combo.addItem("人工智能教程")
        combo.addItem("自动化教程")

        combo.move(50, 50)
        self.lbl.move(50, 200)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('组合框')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


app = QApplication(sys.argv)
ex = ComboBoxExample()
app.exec_()
