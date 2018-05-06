from multiprocessing.managers import BaseManager
import time,queue

task_queue = queue.Queue()

def get_task():
    global task_queue
    return task_queue

def conncet_s():
    BaseManager.register('task_queue',callable=get_task)
    #必须前面加b，否则会出现string argument without an encoding的bug
    #b前缀没什么具体意义， 只是为了兼容python3.x的这种写法
    manager = BaseManager(address=('127.0.0.1',9999),authkey=b'zjk')
    manager.start()
    return manager


if __name__  =="__main__":
    server = conncet_s()
    n = 0
    while 1:
        print('number is :%d'%n)
        task = server.task_queue()
        task.put(n)
        time.sleep(1)
        n = n+1
    server.shutdown
