import requests
import pygal
from random import randint
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from random_langugage import RandomLanguage

RL = RandomLanguage()
print(f'Creating a {RL.language_title} chart...')

# Make an API request and store response
url = f'https://api.github.com/search/repositories?q=language:{RL.language}&sort=stars'
r = requests.get(url)
print('API Request Status: ', r.status_code)

# Store API response in a variable
response_dict = r.json()
print('Total repositories: ', response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'] or "",
        'xlink': repo_dict['html_url'],
    }

    plot_dicts.append(plot_dict)

# Visualize with pygal bar chart
my_style = LS(RL.language_color, base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.value_formatter = lambda y: f'{y:,.0f}'  # format (123,456)
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.tooltip_fancy_mode = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = f'Most-Starred {RL.language_title} Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file(
    f'./working_with_apis/images/svg/{RL.language}_repos.svg')
print(f'Created a {RL.language_title} chart.')
