import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication)


class QCalendarWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('日历')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


app = QApplication(sys.argv)
ex = QCalendarWidgetExample()
app.exec_()
