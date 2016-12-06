# coding:utf-8
# author:cnxuan05
'''
守护线程slave 服务于 非守护线程master
进程至少包含一个线程
queue 解耦 使程序实现松耦合 == 生产者 消费者模型
io 操作不占用cpu
计算 占用cpu
python 多线程不适合cpu密集型的任务 适合io密集型的任务

'''

import time
import threading
import multiprocessing
from multiprocessing import Process

def thread_run():
    print(threading.get_ident())
def run(n):
    time.sleep(2)
    print('run thread...', n)
    t = threading.Thread(target=thread_run,)
    t.start()

def func01():
    t_res = []

    for i in range(10):
        t = threading.Thread(target=run, args=(n,))
        t.setDaemon(True)
        t.start()
        # t_res.append(t)
    # for r in t_res:
    #    r.join()
    print('master is done....')


def func02():

    for u in range(10):
        p = multiprocessing.Process(target=run, args=('bob %s'% u,))
        p.start()
    pass


def func03():

    pass