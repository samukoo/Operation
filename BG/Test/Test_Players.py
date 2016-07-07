#Test class for player and players
import unittest
from BG.Game.Players.Players import Players
from BG.Exceptions.BGExceptions import *

class TestPlayers(unittest.TestCase):

    players = Players()

    def setUp(self):
        del self.players.players[:]

    def test_create_player(self):
        self.players.create_player("Sauli")
        u = self.players.players[0]
        self.assertEqual('Sauli', u.get_name())

    def test_two_players_cant_have_same_name(self):
        self.players.create_player("Sauli")
        with self.assertRaises(PlayerExistException):
            self.players.create_player('Sauli')
        self.assertEqual(1, self.players.players.__len__())

    def test_list_can_have_two_players(self):
        self.players.create_player('Sauli')
        self.players.create_player('Anna')
        self.players.list_players()

        for p in self.players.players:
            if p.get_name() is 'Anna':
                p.co.add_unit('infantry', 10)
                p.co.add_unit('infantry', 10)
                p.co.add_unit('tank', 10)

            elif p.get_name() is 'Sauli':
                p.co.add_unit('tank', 10)
                p.co.add_unit('infantry', 10)

        for p in self.players.players:
            if p.get_name() is 'Anna':
                print 'Anna*s units:'
                print p.co.count_units()
                self.assertEqual(3, p.co.count_units())
                p.co.list_units()
            if p.get_name() is 'Sauli':
                print 'Sauli*s units:'
                print p.co.count_units()
                self.assertEqual(2, p.co.count_units())
                p.co.list_units()

    def test_user_can_buy_units(self):
        self.players.create_player('Sauli')
        self.players.create_player('Anna')
        self.assertEqual(True, self.players.buy_unit('Sauli','tank'))
        self.assertEqual(True, self.players.buy_unit('Anna','infantry'))
        for p in self.players.players:
            print p.get_name()
            p.co.list_units()
            self.assertEqual(1,p.co.count_units())

    def test_buying_units_deduct_credits(self):
        self.players.create_player('Sauli')
        self.players.buy_unit('Sauli', 'infantry')
        for p in self.players.players:
            if p.get_name() is 'Sauli':
                print p.get_credits()
                self.assertEqual(9, p.get_credits())


