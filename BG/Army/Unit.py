# Unit class

class Unit(object):

    def __init__(self, name, cost, damage = 10):
        self.damage = damage
        self.name = name
        self.cost = cost
    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def get_cost(self):
        return self.cost

    def do_damage(self, damage):
        self.damage = self.damage - damage
        print 'Unit %s has %s hit points left' % (self.name, self.damage)