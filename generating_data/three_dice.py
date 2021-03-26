import pygal

from die import Die


# Create 3 D6 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Max possible value of rolled dice
min_result = (3)
max_result = (die_1.num_sides + die_2.num_sides + die_3.num_sides)

# Store results, and frequencies of results in lists
results = [die_1.roll() + die_2.roll() + die_3.roll()
           for roll_n in range(10**6)]
frequencies = [results.count(result)
               for result in range(min_result, max_result+1)]

# Create bar chart with pygal
hist = pygal.Bar()

hist.title = 'Result of rolling three D6 dice 10^6 times.'
hist.x_labels = [label for label in range(min_result, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('./generating_data/images/svg/three_dice.svg')
