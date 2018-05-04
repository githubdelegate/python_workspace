
from flask import Flask,jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook
import json

app = Flask(__name__)
app.config.from_object('config')

@app.route('book/seatch/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keywork(q)

    return jsonify(result)
    # return json.dump(result), 200, {'content-type':'application/json'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)