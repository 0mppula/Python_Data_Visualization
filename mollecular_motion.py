import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
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
    plt.show()

    new_figure = input('Do you want to plot a new chart? (y/n): ')
    if new_figure == 'N' or new_figure == 'n':
        break
