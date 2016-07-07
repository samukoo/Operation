# mechanics for the game

from BG.Army.Commander import Commander

class Mechanics(object):

    def update_units(self, units):
        """
        Update units list by removing units from the list, that has 0 or less damage left
        :param units:
        :return units:
        """
        for unit in units:
            if unit.get_damage() <= 0:
                print 'Unit "%s" eliminated' % (unit.get_name())
                units.remove(unit)
        return units