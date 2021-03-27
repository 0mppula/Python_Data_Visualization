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
data_file = './data/sitka_weather_07-2014.csv'

with open(data_file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lows, highs = [], [], []
    for row in reader:
        date = (row[0])
        high = int(row[1])
        low = int(row[2])
        date_formatted = str_to_date(date)
        high_c = fahrenheit_to_celsius(high)
        low_c = fahrenheit_to_celsius(low)
        dates.append(date_formatted)
        highs.append(high_c)
        lows.append(low_c)


# Plot data with matplotlib
fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(dates, highs, c='red')

plt.title('Daily High In Sitka Tempratures, July 2014', fontsize=20)
plt.xlabel('', fontsize=14)
plt.ylabel('Temperature (C)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.locator_params(axis='x', nbins=10)
fig.autofmt_xdate()

plt.show()
