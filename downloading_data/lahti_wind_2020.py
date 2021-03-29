import csv
from datetime import datetime

import matplotlib.pyplot as plt


# Store wind data in list
lahti_wind_data = './downloading_data/data/lahti_weather_2020.csv'
dates, wind_data = [], []

with open(lahti_wind_data) as f:
    reader = csv.reader(f)
    row_header = next(reader)

    for row in reader:
        try:
            date = datetime.strptime(row[1], '%m/%d/%Y')
            wind = float(row[10])

        except ValueError:
            print(f'Missing data for {date}.')

        else:
            dates.append(date)
            wind_data.append(wind)


# Plot data
fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(dates, wind_data, c=(0.20, 0.20, 0.55, 0.80), label='Wind Speed')

title = 'Wind Speeds 2020 - Lahti, Finland'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=13)
plt.ylabel('Wind Speed (Km/h)', fontsize=13)
plt.tick_params(axis='both', which='both', labelsize=13)

plt.margins(x=0, y=0.1)
fig.autofmt_xdate()

plt.savefig('./downloading_data/images/lahti_wind_2020.png')
plt.show()
