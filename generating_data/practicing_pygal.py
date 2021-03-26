import pygal
import numpy
from pygal.style import Style

from random_walk import RandomWalk

custom_style = Style(
    background='transparent',
    plot_background='#ffffff',
    foreground='#1b1b1b',
    foreground_strong='#1b1b1b',
    foreground_subtle='#1b1b1b',
    opacity='.4',
    opacity_hover='.6',
    colors=('#1b1b1b', '#733380', '#22ff33'))

iterations = 1000
rw = RandomWalk(iterations)
rw.fill_walk()

# Visualize data with pygals's bar chart
hist = pygal.Bar(fill=True, interpolate='cubic',
                 style=custom_style, max_scale=100)

hist.title = f'Visualization of {str(iterations)} random movement iterations.'
hist.x_title = 'Iterations'
hist.y_title = 'Distance'

hist.x_labels = [label if label %
                 500 == 0 else '' for label in range(iterations+1)]


hist.add('X-Distance', rw.x_values)
hist.add('Y-Distance', rw.y_values)
hist.render_to_file('./generating_data/images/svg/bar.svg')
