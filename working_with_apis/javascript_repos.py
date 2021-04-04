import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def get_response():
    """ Make an API request an return response. """
    url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
    r = requests.get(url)
    print('API Request Status: ', r.status_code)
    return r


def get_repo_dicts(response):
    """ Store and return respose dictionary. """
    response_dict = response.json()
    repo_dicts = response_dict['items']
    print('Total repositories: ', response_dict['total_count'])
    return repo_dicts


def get_names_plot_dicts(repo_dicts):
    """ Process the response dicts, store and return names and plot dicts. """
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        name = repo_dict['name']
        names.append(name)

        description = repo_dict['description']
        if not description:
            description = 'No description provided.'

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': description,
            'xlink': repo_dict['html_url'],
        }

        plot_dicts.append(plot_dict)
    return names, plot_dicts


def make_visualization(names, plot_dict):
    """ Make a visualization of data with pygal bar chart. """
    my_style = LS('#733380', base_style=LCS)
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
    chart.title = 'Most-Starred JavaScript Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('./working_with_apis/images/svg/javascript_repos.svg')


r = get_response()
repo_dicts = get_repo_dicts(r)
names, plot_dicts = get_names_plot_dicts(repo_dicts)
make_visualization(names, plot_dicts)
