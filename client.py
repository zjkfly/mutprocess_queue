import time
from multiprocessing.managers import BaseManager

def connect_s():
    BaseManager.register('task_queue')
    client = BaseManager(address=('127.0.0.1',9999),authkey=b'zjk')
    client.connect()
    return client

if __name__ =='__main__':
    manager = connect_s()
    task = manager.task_queue()
    while 1 :
        if task.empty():
            time.sleep(2)
        n = task.get()
        time.sleep(1)
        print('now the number is :%d'%n)

    manager.shutdown()
