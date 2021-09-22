import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)


class GridLayoutExample2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        titleLabel = QLabel('标题')
        authorLabel = QLabel('作者')
        contentLabel = QLabel('内容')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)  # 设置组件之间的间距

        grid.addWidget(titleLabel, 1, 0)  # 布局在第 1 行第 0 列
        grid.addWidget(titleEdit, 1, 1)  # 布局在第 1 行第 1 列

        grid.addWidget(authorLabel, 2, 0)  # 布局在第 2 行第 0 列
        grid.addWidget(authorEdit, 2, 1)  # 布局在第 2 行第 1 列

        grid.addWidget(contentLabel, 3, 0)  # 布局在第 3 行第 0 列
        grid.addWidget(contentEdit, 3, 1, 5, 1)  # 布局在第 3 行第 1 列，跨越 5 行 1 列

        self.setLayout(grid)

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('网格布局2')
        self.show()


app = QApplication(sys.argv)
ex = GridLayoutExample2()
app.exec_()
