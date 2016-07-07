import unittest
from BG.Game.Players.Player import Player

class TestPlayer(unittest.TestCase):

    def test_player_has_co(self):
        self.assertEqual(0, self.p.co.count_units())

    def test_player_has_credits_when_created(self):
        self.assertEqual(10, self.p.get_credits())

    def test_individual_player_can_have_army(self):
        self.p.co.add_unit('tank',10)
        self.p.co.add_unit('tank',10)
        self.assertEqual('Sauli', self.p.get_name())
        self.assertEqual(2, self.p.co.count_units())

    def test_credit_deduct(self):
        self.p.deduct_credits(5)
        self.assertEqual(5, self.p.get_credits())

    def setUp(self):
        self.p = Player('Sauli')


    def tearDown(self):
        del self.p.co.units[:]
        self.p = None
