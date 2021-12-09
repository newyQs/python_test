from multiprocessing import Process, queues
import multiprocessing


def func(data, share_data):
    share_data.put(data)


if __name__ == '__main__':

    share_data = queues.Queue(1, ctx=multiprocessing)

    p = Process(target=func, args=('learning python', share_data))
    p.start()
    p.join()

    print(share_data.get())
'''
 关于队列（queues），上面我们指定队列里面只能放入一个元素，
 如果超过一个，再次往队列里面 put 元素时则会阻塞，直到队列的元素被取出，才能放进去
'''