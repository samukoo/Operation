# damage class to handle unit damage

from BG.Army.Commander import Commander

class Damage(object):

    def calc_damage(self, units, index, dmg):
        """
        Updates units damage
        :param index: Unit index in list
        :param dmg: Damage count
        """
        unit = units.pop(index)
        print '%s is taking %s damage ' % (unit.name, dmg)
        unit.do_damage(dmg)
        units.insert(index, unit)
        return units
