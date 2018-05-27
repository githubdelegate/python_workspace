
from collections import  namedtuple

from app.view_models.book import BookViewModel

# 这个viewmodel 对应的 我的礼物页面 里面的view的

# 这个model 对应显示的每个行的信息，包括 一个book的详细信息，和想要数量
MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


# 这个代表整体的页面 全部model
class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self._gifts_of_mine = gifts_of_mine
        self._wish_count_list = wish_count_list
        self._parse()

    def _parse(self):
        for gift in self._gifts_of_mine:
            my_gift = self._matching(gift)
            self.gifts.append(my_gift)

    def _matching(self, gift):
        count = 0
        for wish_count in self._wish_count_list:
            if gift.isbn == wish_count['sibn']:
                count = wish_count['count']
        my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        return  my_gift

