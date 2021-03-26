import pygal

from die import Die

# Create two D8 dice
die_1 = Die(8)
die_2 = Die(8)

# Max possible result of rolled dice
min_result = 2
max_result = die_1.num_sides + die_2.num_sides

# Store results of rolls in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(10**6)]

# Store frequencies of roll in a list
frequencies = [results.count(result)
               for result in range(min_result, max_result + 1)]

hist = pygal.Bar()

hist.title = 'Result of rolling two D8 dice 10^6 times.'
hist.x_labels = [label for label in range(min_result, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D8 + D8', frequencies)
hist.render_to_file('./generating_data/images/svg/2_d8_visual.svg')
