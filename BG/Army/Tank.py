# Tank class
# Tank cost is 4 credits
from Unit import Unit

class Tank(Unit):

    def __init__(self, name, cost = 4):
        super(Tank, self).__init__(name, cost)