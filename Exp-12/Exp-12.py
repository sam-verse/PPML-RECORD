import matplotlib.pyplot as plt
from scipy import stats

# Original data points
x_data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y_data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Calculate linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)

# Define linear regression function
def linear_regression(x):
    return slope * x + intercept

# Generate model values
model_values = [linear_regression(x) for x in x_data]

# Plot original data points and regression line
plt.scatter(x_data, y_data)
plt.plot(x_data, model_values)
plt.show()
