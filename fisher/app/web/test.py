class test:
    # def __enter__(self):
    #     print('__enter__')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('__exit__')


    def query(self):
        print('query')



# with test() as t:
#     t.query()



# 上下文管理器，
#  contextmanager 的作用是把一个类 装饰成上下文管理器 ，而不需要修改原来的类的代码
from contextlib import contextmanager
@contextmanager
def make_test():
    print('begin')
    yield test()
    print('end')


with make_test() as t:
    t.query()