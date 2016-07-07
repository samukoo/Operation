# Players class
# Class for player objects
# Higher level interface for manipulating User / Commander objects
from Player import Player
from BG.Exceptions.BGExceptions import *
class Players(object):

    players = list()

    def create_player(self, name):
        if self.__check_names(name,self.players) is False:
            raise PlayerExistException()
        else:
            self.players.append(Player(name))
            print 'Player %s created' % name

    def list_players(self):
        i = 1
        for player in self.players:
            print 'player nr.%s: %s' % (i, player.get_name())
            i=i+1

    def buy_unit(self, name, item):
        """
        Buys unit for player
        :param name: Player's name
        :param item: Item player buy
        :return: boolean
        """
        for player in self.players:
            if player.get_name() is name:
                try:
                    player.deduct_credits(player.co.add_unit(item, player.get_credits()))
                except CreditExceededException, c:
                    print c.msg
                return True
        return False

    def get_player(self, name):
        for player in self.players:
            if player.get_name() is name:
                print 'returning %s' % (player.get_name())
                return player

    def __check_names(self, name , list):
        for item in list:
            if name == item.get_name():
                print 'Error code 1: User with same name exists. pick new'
                return False
        return True
