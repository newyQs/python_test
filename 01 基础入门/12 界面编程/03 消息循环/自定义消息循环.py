import sys

msg = []  # 用全局变量定义一个消息队列


class MsgLoop(object):
    def __init__(self):
        super(MsgLoop, self).__init__()

    def getmessage(self):
        try:
            newmsg = msg[0]
            del msg[0]
            return newmsg
        except:
            return

    def msg_clicked(self):
        print("do clicked msg")

    def msg_keydown(self):
        print("do keydown msg")  # 处理键盘消息

    def msg_mousemove(self):
        print("do mousemove msg")  # 处理鼠标移动消息

    def msgcheck(self):
        while True:
            onemsg = input("投递一个消息：")  # 输入要模拟的消息
            msg.append(onemsg)  # 投递消息
            newmsg = self.getmessage()  # 从消息队列里面取出消息

            if newmsg == "clicked":
                self.msg_clicked()  # 处理点击消息

            elif newmsg == "keydown":
                self.msg_keydown()  # 处理键盘消息

            elif newmsg == "mousemove":
                self.msg_mousemove()  # 处理鼠标移动消息

            else:
                pass


class MyApplication(object):
    def __init__(self, argv):
        super(MyApplication, self).__init__()
        self.msgloop = MsgLoop()

    def _exec(self):
        self.msgloop.msgcheck()  # 我们自定义的消息循环


app = MyApplication(sys.argv)  # 类似 qt 的 app = QApplication(sys.argv)
print("显示界面")
app._exec()  # 进入消息循环
