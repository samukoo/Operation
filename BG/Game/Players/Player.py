# Player class

from BG.Army.Commander import Commander

class Player(object):

    def __init__(self, name, credits = 10):
        self.__name = name
        self.__credits = credits
        self.co = self.__create_commander()

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def deduct_credits(self, deduct):
        self.__credits = self.__credits - deduct

    def __create_commander(self):
        return Commander()