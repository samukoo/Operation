# Commander class
from BG.Exceptions.BGExceptions import CreditExceededException
from Tank import Tank
from Infantry import Infantry

class Commander(object):


    def __init__(self):
        self.units = list()
        print "Init commander"

    def add_unit(self, unit, credits):
        if unit == "infantry":
            u = Infantry('Jaeger')
            if u.get_cost() <= credits:
                self.units.append(u)
                return u.get_cost()
        elif unit == "tank":
            u = Tank('Panzer')
            if u.get_cost() <= credits:
                self.units.append(u)
                return u.get_cost()
            else:
                raise CreditExceededException(u.get_cost(), credits)
        else:
            return "unit not found"

    def count_units(self):
        """
        Prints total count of units
        """
        return self.units.__len__()

    def list_units(self):
        """
        Prints current units
        """
        for unit in self.units:
            print 'Unit name: %s. Unit condition: %s hit points.' % (unit.get_name(), unit.get_damage())
