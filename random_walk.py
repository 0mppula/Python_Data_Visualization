from random import choice


class RandomWalk():
    """ Class for generating random walks. """

    def __init__(self, num_points=5000):
        """ Initialize attributes of a walk. """
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Calculate all points in the walk. """

        # Keep taking steps untill the walk reaches desired lenght.
        while len(self.x_values) < self.num_points:
            # Decision which direction to go and how far to go in that direction
            x_direction = choice([-1, 1])
            x_distance = choice([1, 2, 3, 4, 5])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
