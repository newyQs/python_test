import sys
import calui
from decimal import Decimal
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap


class MyWidget(QWidget):
    def initdata(self):  # 初始化数据
        self.operator = ""  # 运算符
        self.leftdata = ""  # 左边数据
        self.rightdata = ""  # 右边数据
        self.bcalculated = False  # 有没有做运算
        self.error = False  # 错误的计算，比如除数为0

    def initui(self):
        self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        self.setWindowIcon(QIcon('birdpython.png'))  # 设置窗口图标
        self.ui.lineEdit_rst.setText("0")  # 结果栏里默认为 0

        # 给窗口设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("background.png")))
        self.setPalette(palette)

        # 给链接按钮设置颜色
        self.ui.pushButton_link.setStyleSheet('QPushButton {background-color: green}')

    def __init__(self):
        self.initdata()
        super(MyWidget, self).__init__()
        self.ui = calui.Ui_Form()
        self.ui.setupUi(self)
        self.initui()

        # 数字信号槽关联
        self.ui.pushButton_1.clicked.connect(self.clicked_num)
        self.ui.pushButton_2.clicked.connect(self.clicked_num)
        self.ui.pushButton_3.clicked.connect(self.clicked_num)
        self.ui.pushButton_4.clicked.connect(self.clicked_num)
        self.ui.pushButton_5.clicked.connect(self.clicked_num)
        self.ui.pushButton_6.clicked.connect(self.clicked_num)
        self.ui.pushButton_7.clicked.connect(self.clicked_num)
        self.ui.pushButton_8.clicked.connect(self.clicked_num)
        self.ui.pushButton_9.clicked.connect(self.clicked_num)
        self.ui.pushButton_0.clicked.connect(self.clicked_num)

        # 运算
        self.ui.pushButton_plus.clicked.connect(self.clicked_calculate)
        self.ui.pushButton_minus.clicked.connect(self.clicked_calculate)
        self.ui.pushButton_multiply.clicked.connect(self.clicked_calculate)
        self.ui.pushButton_divide.clicked.connect(self.clicked_calculate)

        # 官网
        self.ui.pushButton_link.clicked.connect(self.clicked_link)

        # 归零
        self.ui.pushButton_clear.clicked.connect(self.clicked_clear)

        # 小数点
        self.ui.pushButton_dot.clicked.connect(self.clicked_dot)

        # 等号
        self.ui.pushButton_rst.clicked.connect(self.clicked_result)

    def clicked_link(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://www.birdpython.com'))

    def clicked_dot(self):  # 小数点
        if self.bcalculated == True:  # 右边数
            if self.rightdata == "":
                self.rightdata = "0."
            else:
                self.rightdata += "."
            self.ui.lineEdit_rst.setText(self.rightdata)
        else:  # 左边数
            if self.leftdata == "":
                self.leftdata = "0."
            else:
                self.leftdata += "."
            self.ui.lineEdit_rst.setText(self.leftdata)

    def clicked_clear(self):  # 清零
        self.initdata()
        self.ui.lineEdit_rst.setText("0")  # 结果栏里默认为 0

    def clicked_num(self):
        sender = self.sender()  # sender 是发射信号的按钮

        if self.bcalculated == True:  # 右边数
            if (self.rightdata == "0" or self.rightdata == "") and sender.text() == "0":
                self.ui.lineEdit_rst.setText("0")
            else:
                self.rightdata += sender.text()  # 右边数字
                self.ui.lineEdit_rst.setText(self.rightdata)
        else:  # 左边数
            if self.ui.lineEdit_rst.text() == "0" and sender.text() == "0":
                self.ui.lineEdit_rst.setText("0")
            else:
                self.leftdata += sender.text()  # 左边数字
                self.ui.lineEdit_rst.setText(self.leftdata)

    def clicked_result(self):  # 点击等号
        if self.error:  # 除数为0
            self.initdata()
            self.error = True
            self.ui.lineEdit_rst.setText("除数不能为0，请归零后重新开始")
        else:
            self.ui.lineEdit_rst.setText(str(self.getresult()))

    def getresult(self):  # 计算结果
        # 把空值转为 "0"
        self.leftdata = self.leftdata if self.leftdata != "" else "0"
        self.rightdata = self.rightdata if self.rightdata != "" else "0"

        try:
            self.leftdata = Decimal(self.leftdata)
            self.rightdata = Decimal(self.rightdata)
        except:
            return self.leftdata

        if self.operator == "+":
            self.leftdata += self.rightdata  # 左数据为运算结果
        elif self.operator == "-":
            self.leftdata -= self.rightdata
        elif self.operator == "×":
            self.leftdata *= self.rightdata
        elif self.operator == "^":
            self.leftdata = pow(self.leftdata, self.rightdata)
        elif self.operator == "÷":
            if self.rightdata == 0:
                self.initdata()
                self.error = True
                return
            self.leftdata /= self.rightdata

        self.rightdata = ""
        self.leftdata = str(self.leftdata)
        return self.leftdata

    def clicked_calculate(self):
        if self.bcalculated == True:  # 点击过运算和被运算的数字了
            rst = str(self.getresult())
            if self.error:  # 除数为0
                self.ui.lineEdit_rst.setText("除数不能为0，请归零后重新开始")
            else:
                self.ui.lineEdit_rst.setText(rst)

        sender = self.sender()  # sender 是发射信号的按钮
        self.operator = sender.text()
        self.bcalculated = True


app = QApplication(sys.argv)
mycal = MyWidget()
mycal.show()
app.exec_()
