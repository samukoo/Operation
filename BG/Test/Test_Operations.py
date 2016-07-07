# Test class

import unittest
from BG.Exceptions.BGExceptions import *
from BG.Army.Commander import Commander
from BG.Operations.Damage import Damage
from BG.Operations.Mechanics import Mechanics

class TestOperations(unittest.TestCase):

    co = Commander()
    dmg = Damage()
    mechanics = Mechanics()

    def setUp(self):
        del self.co.units[:]

    def test_no_credits_throws_exception(self):
        with self.assertRaises(CreditExceededException):
            self.co.add_unit('tank',3)

    def test_buy_units(self):
        expected = 2
        self.co.add_unit("tank",10)
        self.co.add_unit("infantry",10)
        self.assertEquals(expected, self.co.count_units(), "List should have 2 units")

    def test_hit_causes_damage(self):
        self.co.add_unit("tank",10)
        self.assertEqual(1,self.co.count_units())
        self.co.units = self.dmg.calc_damage(self.co.units,0,8)
        unit = self.co.units[0]
        self.assertEqual(2, unit.get_damage())

    def test_destroyed_unit_is_removed_from_list(self):
        self.co.add_unit("tank",10)
        self.assertEqual(1,self.co.count_units())
        self.co.units = self.dmg.calc_damage(self.co.units,0,10)
        unit = self.co.units[0]
        self.assertEqual(0, unit.get_damage())
        self.co.units = self.mechanics.update_units(self.co.units)
        self.assertEqual(0, self.co.count_units())

    def test_destroy_unit_from_units(self):
        self.co.add_unit("tank",10)
        self.co.add_unit("infantry",10)
        self.assertEqual(2,self.co.count_units())
        print self.co.list_units()
        self.co.units = self.dmg.calc_damage(self.co.units,1,10)
        self.co.units = self.mechanics.update_units(self.co.units)
        self.assertEqual(1,self.co.count_units())
        print self.co.list_units()

    def test_name_and_damage_is_printed(self):
        self.co.add_unit("tank",10)
        unit = self.co.units[0]
        self.assertEqual(10,unit.get_damage())
        self.assertEqual('Panzer', unit.get_name())