import csv
from matplotlib import pyplot as plt
from datetime import datetime


def fahrenheit_to_celsius(temp):
    """ Convert given fahrenheit temp to celsius. """
    celsius_temp = ((temp - 32) * 5 / 9)
    return round(celsius_temp, 2)


def str_to_date(string):
    """Format given string to date object. """
    formatted_date = datetime.strptime(string, '%Y-%m-%d')
    return formatted_date


# Get dates and high and low tempratures from file
data_file = './data/death_valley_2014.csv'

with open(data_file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lows, highs = [], [], []
    for row in reader:
        try:
            date = (row[0])
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print(f'{date} missing data')

        else:
            date_formatted = str_to_date(date)
            high_c = fahrenheit_to_celsius(high)
            low_c = fahrenheit_to_celsius(low)
            dates.append(date_formatted)
            highs.append(high_c)
            lows.append(low_c)


# Plot data with matplotlib
fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
plt.title(title, fontsize=18)
plt.xlabel('', fontsize=13)
plt.ylabel('Temperature (C)', fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)

plt.margins(x=0, y=0.1)
fig.autofmt_xdate()

plt.savefig('./data/images/high_low_death_valley.png')
plt.show()
