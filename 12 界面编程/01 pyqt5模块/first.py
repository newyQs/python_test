import sys
from PyQt5.QtWidgets import QApplication, QWidget


def myWidget():
    # 每一 pyqt5 应用程序必须创建一个应用程序对象。sys.argv 参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)

    # 创建一个基于 QWidget 的部件（该部件类似对话框）。
    w = QWidget()

    # 调整窗口的大小。这里是 800 px宽，500px高
    w.resize(800, 500)

    # move()方法移动窗口在屏幕上的位置到 x=600，y=200 坐标。
    w.move(600, 200)

    # 设置窗口的标题
    w.setWindowTitle('第一个界面程序')

    # 显示 QWidget 部件
    w.show()

    '''
    app.exec_() 里面是一个死循环，也叫作消息循环，任何界面程序都使用的一种技术
    在该消息循环里，QWidget 部件就可以接受和处理消息（比如最大化窗口，拖动窗口等等）
    '''
    app.exec_()


myWidget()
