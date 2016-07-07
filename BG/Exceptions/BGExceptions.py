
class CreditExceededException(Exception):

    def __init__(self, price, credits):
        self.msg = 'Not enough credits! %s short' % (credits - price)

class PlayerExistException(Exception):

    def __init__(self):
        self.msg = "Player with same name already exist!"