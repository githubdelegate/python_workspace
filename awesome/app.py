
from aiohttp import web
import time,threading
import mysql.connector
import asyncio 

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



def consumer():
    print('def con')
    r = ''
    print('r = ')
    while True:
        print('49')
        n = yield r
        print('51')
        if not n:
            return
        print('[consume] consuming %s...' % n)
        r = '200ok'

def product(c):
    print('def pro')
    c.send(None)
    print('n =0')
    n = 0
    print('62')
    while n < 5:
        n = n + 1
        print('[Product] producting %s ...' % n)
        r = c.send(n)
        print('[Product] Cosumer return %s' % r)
    c.close()




@asyncio.coroutine
def wget(host):
    print('wget %s ...' % host)
    conect = asyncio.open_connection(host,80)
    reader,writer = yield from conect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
    writer.close()




if __name__=='__main__':
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.cn','www.sohu.com','www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    










