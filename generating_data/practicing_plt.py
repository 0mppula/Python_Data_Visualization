import matplotlib.pylab as plt
import pygal

from die import Die

# Create Dice
die_1 = Die(8)
die_2 = Die(8)

# Min & max results
min_result = 2
max_result = (die_1.num_sides + die_2.num_sides)
roll_count = 1000

# Store rolls and frequencies in lists
results = [die_1.roll() + die_2.roll() for roll_num in range(roll_count)]
x_values = [x_value for x_value in range(min_result, max_result + 1)]
y_values = [results.count(frequency)
            for frequency in range(min_result, max_result + 1)]


def plot_line(x_values, y_values):
    """ Plots data to matplotlib's line chart. """
    plt.figure(dpi=110, figsize=(10, 6))
    plt.plot(x_values, y_values, c=(0.22, 0.22, 0.22), linewidth=3)

    plt.title(f'Result of rolling 2 D8 dice {str(roll_count)} times.', color=(
        0.8, 0.15, 0.15), fontsize=20)
    plt.xlabel('Result', color=(0.8, 0.15, 0.15), fontsize=12)
    plt.ylabel('Frequency of Result', color=(0.8, 0.15, 0.15), fontsize=12)
    plt.axis([min_result, max_result, 0, (max(y_values) * 1.1)])
    plt.tick_params(axis='both', labelsize=10)

    plt.fill_between(x_values, y_values, color=(0.30, 0.30, 0.30, 0.5))
    plt.tight_layout()
    plt.show()


plot_line(x_values, y_values)
