import matplotlib.pyplot as plt


x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(9, 6))
plt.scatter(x_values, y_values, edgecolors=None,
            c=y_values, cmap=plt.cm.YlOrRd, s=3)

# Labels and axis
plt.title('Cubes of Numbers', fontsize=22)
plt.xlabel('Number', fontsize=14)
plt.ylabel('Value of Cube', fontsize=14)

# Tick label size
plt.tick_params(axis='both', which='major', labelsize=14)

# x, y axis range
plt.axis([0, 5500, 0, 5100**3])

plt.savefig('./generating_data/images/cubes_plot_5000.png')
plt.show()
