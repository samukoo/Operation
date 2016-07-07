# Infantry class
# Infantry cost = 1 credit
from Unit import Unit

class Infantry(Unit):

    def __init__(self, name, cost = 1):
        super(Infantry, self).__init__(name, cost)
