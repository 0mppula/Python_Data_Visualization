import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336699', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['public-apis', 'Python-100-Days', 'awesome-python']

plot_dicts = [
    {'value': 115834, 'label': 'Description of public-apis'},
    {'value': 101243, 'label': 'Description of Python-100-Days'},
    {'value': 95436, 'label': 'Description of awesome-python'},
]

chart.add('', plot_dicts)
chart.render_to_file('./working_with_apis/images/svg/bar_descriptions.svg')
