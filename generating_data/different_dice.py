import pygal

from die import Die


# Create dice
die_1 = Die()
die_2 = Die(10)

# Max value of rolled dice
max_result = die_1.num_sides + die_2.num_sides

# Make some rolls, and store the values in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

# Analyze the results
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the result
hist = pygal.Bar()

hist.title = 'Result of rolling a D6 and D10 die 50000 times.'
hist.x_labels = [n for n in range(2, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('./generating_data/images/svg/dice_visual.svg')
