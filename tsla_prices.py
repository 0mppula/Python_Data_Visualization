import matplotlib.pyplot as plt

x_values = ['17/3', '18/3', '19/3', '22/3', '23/3']
y_values = [701.81, 653.16, 654.87, 670, 662.16]
plt.scatter(x_values, y_values, c=(0.9, 0.1, 0.1), s=100)

# Set chart title and label axes
plt.title('TSLA 5 Day Price Movement', fontsize=22)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Price $', fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)


plt.savefig('./images/1week_tsla_price.png', bbox_inches='tight')
plt.show()
