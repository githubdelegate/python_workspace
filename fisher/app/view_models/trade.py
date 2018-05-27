from datetime import date

class TradeInfo:

    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = date.fromtimestamp(single.create_time).strftime('%Y-%m-%d')
        else:
            time = 'unkonw'

        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )

