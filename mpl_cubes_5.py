import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]
red = (0.9, 0.1, 0, 1)
plt.plot(x_values, y_values, c=red, linewidth=2)

# Titles
plt.title('Cubes of Numbers', fontsize=22)
plt.xlabel('Number', fontsize=14)
plt.ylabel('Values of Cubes', fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)


plt.show()

print(y_values)
