import csv
from datetime import datetime

import matplotlib.pyplot as plt


# Store percipitation data from csv file
dubai_weather_data = './downloading_data/data/dubai_weather_2020.csv'

dates, rain_data = [], []
with open(dubai_weather_data) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            date = datetime.strptime(row[1], '%m/%d/%Y')
            rain = float(row[7])

        except ValueError:
            print(f'missing data for {date}.')

        else:
            dates.append(date)
            rain_data.append(rain)


# Plot data with matplotlib
fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(dates, rain_data, c=(0.2, 0.2, 0.6, 0.75), label='Dubai')

title = 'Percipitation Data 2020 - Dubai, UAE'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=13)
plt.ylabel('Percipitation (mm)', fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)


plt.margins(x=0, y=0.1)
fig.autofmt_xdate()

plt.savefig('./downloading_data/images/dubai_rain_2020.png')
plt.show()
