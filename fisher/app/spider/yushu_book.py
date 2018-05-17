
from app.libs.book_http import BookHTTP
from flask import  current_app

class YuShuBook:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'


    def __init__(self):
        self.total = 0
        self.books = []


    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = BookHTTP.get(url)
        self.__fill_single(result)

    def search_by_keywork(self, keyword,page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = BookHTTP.get(url)
        self.__fill_collection(result)


    def calculate_start(self, page):
        return (page -1) * current_app.config['PER_PAGE']


    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']


    @property
    def first(self):
        return self.books[0] if self.total >=1 else None
