
from aiohttp import web
import time,threading
import mysql.connector

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
    conn = mysql.connector.connect(user='root',password='',database='test')
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
    cursor.execute('insert into user (id,name) values (%s,%s)',['1','maic'])
    conn.commit()
    cursor.close()

    cursor = conn.cursor()
    cursor.execute('select * from user where id =%s',('1',))
    values = cursor.fetchall()
    print('values= %s' % values)
    cursor.close()
    conn.close()
    










