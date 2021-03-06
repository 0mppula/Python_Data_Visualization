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
                if date in dates:
                    pass
                else:
                    date_list.append(date)
                mean_temp_list.append(mean_temp)


# Get date and average temperature data from csv files
lahti = './downloading_data/data/lahti_weather_2020.csv'
san_francisco = './downloading_data/data/san_francisco_weather_2020.csv'
sitka = './downloading_data/data/sitka_weather_2020.csv'

dates = []
lahti_temps = []
san_francisco_temps = []
sitka_temps = []

get_avg_temp_data(san_francisco, dates, san_francisco_temps)
get_avg_temp_data(lahti, dates, lahti_temps)
get_avg_temp_data(sitka, dates, sitka_temps)

# Plot all data in a matplotlib chart
fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(dates, san_francisco_temps,
         c='red', alpha=0.75, label='San Francisco')
plt.plot(dates, lahti_temps, c='blue', alpha=0.75, label='Lahti')
plt.plot(dates, sitka_temps, c='green', alpha=0.75, label='Sitka')

title = 'Average Daily Temperatures in 2020'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=13)
plt.ylabel('Temperature (C)', fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)

plt.margins(x=0, y=0.1)
fig.autofmt_xdate()
plt.legend()

plt.savefig('./downloading_data/images/average_temps_2020.png')
plt.show()
