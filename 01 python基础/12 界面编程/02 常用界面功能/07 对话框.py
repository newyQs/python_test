import sys
from PyQt5.QtWidgets import QApplication, QDialog


class myDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('对话框')
        self.show()


app = QApplication(sys.argv)
demo = myDialog()
app.exec()
