import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
line_color = (0.27, 0.27, 0.27)

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Purples, edgecolors=None, s=5)

# Set chart title and label axes
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])


plt.savefig('./generating_data/images/squares_plot.png', bbox_inches='tight')
plt.show()
