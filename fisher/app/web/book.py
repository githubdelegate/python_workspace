from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from flask import Blueprint

web = Blueprint('web', __name__)


@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keywork(q)

    return jsonify(result)
    # return json.dump(result), 200, {'content-type':'application/json'}
