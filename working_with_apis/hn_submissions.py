import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Meke an API call and store the respose
api_url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
r = requests.get(api_url)
print('Status code: ', r.status_code)

# Process information about each submission
submission_ids = r.json()

titles, submission_dicts = [], []
plot_counter = 0
for submission_id in submission_ids[:30]:
    # Make a seperate API call to for each submission
    url = (
        f'https://hacker-news.firebaseio.com/v0/item/{str(submission_id)}.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    title = response_dict['title']
    titles.append(title)

    submission_dict = {
        'value': response_dict.get('descendants', 0),
        'label': response_dict['title'],
        'xlink': f'http://news.ycombinator.com/item?id={str(submission_id)}',
    }

    submission_dicts.append(submission_dict)
    plot_counter += 1
    print(f'Plotted {title} to chart... ({str(plot_counter)}/30)')

submission_dicts = sorted(
    submission_dicts, key=itemgetter('value'), reverse=True)

# Visualize API data in a pygal bar chart
my_style = LS('#733380')
my_style.title_font_size = 24
my_style.labe_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.value_formatter = lambda y: f'{y:,.0f}'
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.tooltip_fancy_mode = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Active Discussions Currently on Hacker News'
chart.x_labels = titles

chart.add('', submission_dicts)
chart.render_to_file('./working_with_apis/images/svg/hn_submissions.svg')
print('Chart is Ready!')
