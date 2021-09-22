'''
纯手工打造消息队列，消息循环，和消息投递，实现单线程同步和异步
'''

msg = []  # 消息队列


class mySignal(object):  # 自定义消息对象
    def __init__(self, argtype):  # argtype 是消息对象传来的参数
        self.argtype = argtype

    def connect(self, func, syn=True):  # 默认是同步的
        self.asyn = syn
        self.func = func

    def emit(self, arg):
        if type(arg) == self.argtype:
            if self.asyn == True:  # 同步，直接调用槽函数
                self.func(arg)
            else:  # 异步，入消息队列
                msg.append((self.func, arg))
        else:
            print
            "type error"


class Myapp(object):
    def __init__(self):
        super(Myapp, self).__init__()

    def getmessage(self):  # 从消息队列获取一个消息
        try:
            newmsg = msg[-1]
            msg.pop()
            return newmsg
        except:
            return None

    def exec_(self):
        while True:  # 消息循环
            newmsg = self.getmessage()  # 取出一条消息
            if newmsg:
                newmsg[0](newmsg[1])  # func(arg)
            else:
                pass

    def func(self, arg):  # 槽函数
        print("收到参数：%s" % arg)
        print("消息处理完毕")


class MyMain(object):
    sinOut = mySignal(str)

    def __init__(self, main):
        super(MyMain, self).__init__()
        self.main = main
        self.sinOut.connect(main.func)  # 默认同步

    def run(self):
        self.sinOut.emit("老鸟")
        print("消息投递过了")  # 该语句后于槽函数执行


app = Myapp()
mymain = MyMain(app)
mymain.run()
app.exec_()
