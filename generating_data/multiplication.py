import pygal

from die import Die


# Create 2 D6 dice
die_1 = Die()
die_2 = Die()

# Max rolled value from dice
min_value = 2
max_value = (die_1.num_sides * die_2.num_sides)
roll_count = 1000000

# Value of rolled values multiplied with each other
results = [die_1.roll() * die_1.roll() for roll_num in range(roll_count)]
frequencies = [results.count(frequency)
               for frequency in range(min_value, max_value + 1)]

# Plot data to bar chart
hist = pygal.Bar()

hist.title = f'Result of rolling 3 D6 dice {str(roll_count)} times.'
hist.x_labels = [label for label in range(min_value, max_value + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 * D6', frequencies)
hist.render_to_file('./generating_data/images/svg/multiply_2d8.svg')
