import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class GridLayoutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()  # 创建一个网格布局
        self.setLayout(grid)  # 给界面加入网格布局

        # 创建按钮的标签列表
        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # 在网格中创建一个位置列表
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 创建按钮并通过 addWIdget 方法添加到布局中
        for position, name in zip(positions, names):
            if name == '':
                continue

            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('网格布局')
        self.setGeometry(600, 200, 800, 500)
        self.show()


app = QApplication(sys.argv)
ex = GridLayoutExample()
sys.exit(app.exec_())
