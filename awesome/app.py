
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

if __name__=='__main__':
    t = threading.Thread(target=Loop,name='loop')
    t.start()
    t.join()
    print('thread %s ended' % threading.current_thread().name)






