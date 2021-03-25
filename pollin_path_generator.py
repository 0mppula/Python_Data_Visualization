import matplotlib.pyplot as plt

from random_walk import RandomWalk
counter = 0


def check_int_value(integer, less_than, greater_than):
    """ Checks if given integer is under and over given values. """
    less_than = int(less_than)
    greater_than = int(greater_than)
    integer = int(integer)

    if integer < less_than and integer > greater_than:
        return True


while True:
    counter += 1
    plt.close()
    rw = RandomWalk()
    rw.fill_walk()
    data_points = list(range(rw.num_points))

    plt.figure(dpi=110, figsize=(10, 6))
    plt.plot(rw.x_values, rw.y_values, c=(
        0.12, 0.12, 0.12), linewidth=0.5, zorder=1)

    # Start stop dots
    plt.scatter(0, 0, c='green', edgecolors=None, s=35, zorder=2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolors=None, s=35, zorder=2)

    # Hide axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('./images/pollen_path.png')

    # Store ending x, y values
    ending_x = int(rw.x_values[-1])
    ending_y = int(rw.y_values[-1])

    # Breaks loop if ending values of x and y coordinates are with in a 100,
    # points of starting position
    if check_int_value(ending_x, 50, -51) and check_int_value(ending_y, 50, -51):
        plt.savefig('./images/pollen/plot_'f'{counter}')
        plt.show()
        break
