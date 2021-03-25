import pygal

from die import Die


# Create two D6 dice
die_1 = Die()
die_2 = Die()

# Max result of rolled dice
max_result = die_1.num_sides + die_2.num_sides

# Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyze the results and store frequencies in a list
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 dice 1000 times.'
hist.x_labels = [n for n in range(2, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('./generating_data/images/svg/die_visual.svg')
