import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_avg_temp_data(filename, date_list, mean_temp_list):
    """ Gets average daily temperature from csv file,
    and stores data to given location (list) """

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                date = datetime.strptime(row[1], '%m/%d/%Y')
                mean_temp = float(row[4])

            except ValueError:
                print(f'{date} missing data.')

            else:
                date_list.append(date)
                mean_temp_list.append(mean_temp)


# Get date and average temperature data from csv files
lahti = './data/lahti_weather_2020.csv'
san_francisco = './data/san_francisco_weather_2020.csv'
sitka = './data/sitka_weather_2020.csv'


lahti_dates = []
san_francisco_dates = []
sitka_dates = []
lahti_temps = []
san_francisco_temps = []
sitka_temps = []

get_avg_temp_data(san_francisco, san_francisco_dates, san_francisco_temps)
get_avg_temp_data(lahti, lahti_dates, lahti_temps)
get_avg_temp_data(sitka, sitka_dates, sitka_temps)

# Plot all data in a matplotlib chart
fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(san_francisco_dates, san_francisco_temps,
         c='red', alpha=0.75, label='San Francisco')
plt.plot(lahti_dates, lahti_temps, c='blue', alpha=0.75, label='Lahti')
plt.plot(sitka_dates, sitka_temps, c='green', alpha=0.75, label='Sitka')

title = 'Average Daily Temperatures in 2020'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=13)
plt.ylabel('Temperature (C)', fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)

plt.margins(x=0, y=0.1)
fig.autofmt_xdate()
plt.legend()

plt.savefig('./images/average_temps_2020.png')
plt.show()
