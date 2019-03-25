class Card(object):
    def __init__(self, cardID, cardPassword, cardMoney):
        self.cardID = cardID
        self.cardPassword = cardPassword
        self.cardMoney = cardMoney
        self.cardLock = False #默认卡不锁定