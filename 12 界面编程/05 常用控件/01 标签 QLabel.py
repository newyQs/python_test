import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QMovie


class LableExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建4个标签
        label1 = QLabel(self)  # 文本标签
        label2 = QLabel(self)  # 超文本标签
        label3 = QLabel(self)  # 链接标签
        label4 = QLabel(self)  # 图片标签
        label5 = QLabel(self)  # 动画标签

        label1.move(100, 50)
        label2.move(100, 100)
        label3.move(100, 150)
        label4.move(100, 200)
        label5.move(300, 200)

        label1.setText('这是一个文本标签')
        label2.setText('<strong style="color:#ff0000">欢迎来学习python</strong>')
        label3.setText('<a href="www.birdpython.com">python官网</a>')
        label3.setOpenExternalLinks(True)  # 点击超链接可以打开网页
        pic = QPixmap("birdpython.png")  # 确保当前目录下有该图片文件
        label4.setPixmap(pic)  # 把图片加入标签
        movie = QMovie("collect.gif")  # 确保当前目录下有该动画文件
        label5.setMovie(movie)  # 把动画加入标签
        movie.start()  # 播放动画

        self.setGeometry(600, 200, 800, 500)
        self.setWindowTitle('标签')
        self.show()


app = QApplication(sys.argv)
ex = LableExample()
app.exec_()
