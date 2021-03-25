from random import randint


class Die():
    """ A class representing a single die. """

    def __init__(self, num_sides=6):
        """ Initialize die attributes. """
        self.num_sides = num_sides

    def roll(self):
        """ Roll the die. """
        die_value = randint(1, self.num_sides)
        return die_value
