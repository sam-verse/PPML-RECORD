import matplotlib.pyplot as plt
import numpy as np

# Plot with a line
x_line = np.array([0, 6])
y_line = np.array([0, 250])
plt.plot(x_line, y_line)
plt.show()

# Points without a line
x_points = np.array([0, 5])
y_points = np.array([0, 25])
plt.plot(x_points, y_points, marker='p')
plt.show()

# Multiple points
x_multiple = np.array([1, 2, 6, 8])
y_multiple = np.array([3, 8, 1, 10])
plt.plot(x_multiple, y_multiple)
plt.show()

# Default x points
y_default = np.array([3, 8, 1, 10, 5, 7])
plt.plot(y_default)
plt.show()

