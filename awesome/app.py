
from aiohttp import web
import time,threading

def Loop():
    print('thread %s is running' % threading.current_thread().name)
    n = 0 
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance -n

def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()




local_school = threading.local()

def process_thread(name):
    local_school.student = name
    process_student()

def process_student():
    std = local_school.student
    print('hello %s (in %s)' % (std,threading.current_thread().name))

            
if __name__=='__main__':

    t1 = threading.Thread(target=process_thread,args=('alice',),name='thread_a')
    t2 = threading.Thread(target=process_thread,args=('bob',),name='thread_b')
    t1.start()
    t2.start()
    t1.join()
    t2.join()







