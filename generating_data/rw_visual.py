import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Keep generating new walks, as long as the program is active
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))

    plt.figure(dpi=110, figsize=(10, 6))
    plt.scatter(rw.x_values, rw.y_values,
                c=point_numbers, cmap=plt.cm.Greys, edgecolors=None, s=0.1)

    # Start and end
    plt.scatter(0, 0, c='Green',  edgecolors=None, s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolors=None, s=50)

    # Remove the axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('./generating_data/images/random_walk.png')
    plt.show()

    # Check for quit
    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n' or keep_running == 'N':
        break
