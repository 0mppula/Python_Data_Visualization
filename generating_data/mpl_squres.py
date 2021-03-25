import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)


plt.savefig('./generating_data/images/my_first_graph.png')
plt.show()
