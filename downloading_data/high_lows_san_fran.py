import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Get dates and high and low temperatures form csv file
data_file = './data/san_francisco_weather_2020.csv'

with open(data_file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    # Automatically continues from last read row of csv file
    for row in reader:
        try:
            date = datetime.strptime(row[1], '%m/%d/%Y')
            high = float(row[2])
            low = float(row[3])

        except ValueError:
            print(f'{date} missing data.')

        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# Plot data with matplotlib
fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5, label='highs')
plt.plot(dates, lows, c='blue', alpha=0.5, label='lows')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = 'Daily High & Low temperatures - 2020\nSan Francisco, California'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=13)
plt.ylabel('Temperature (C)', fontsize=13)
plt.ylim(-10, 45)
plt.tick_params(axis='both', which='major', labelsize=13),


plt.margins(x=0, y=0.1)
fig.autofmt_xdate()
plt.legend()

plt.savefig('./images/high_low_san_fran.png', bbox_inches='tight')
plt.show()
