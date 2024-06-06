import numpy as np
def gradient_descent(f, initial_point, learning_rate, iterations):
  point = initial_point.copy()
  history = []
  for _ in range(iterations):
    # Compute gradient of the function at the current point 
    gradient = np.array([2 * point[0], 2 * point[1]])
    # Update point using gradient descent update rule
    point = learning_rate* gradient
    # Calculate the value of the function at the updated point
    value = f(point[0], point[1])
    # Save the history of points and function values
    history.append((point.copy(), value))
    print("Values of points and objective function value are: {} and {}".format(point, value))
  return point, history
def objective_function(x, y):
  return x**2 + y**2 + 4
# Define initial point, learning rate, and number of iterations
initial_point = np.array([1.0, 1.0])
learning_rate=0.1
iterations = 100
# Run gradient descent
minimum_point, history = gradient_descent(objective_function, initial_point, learning_rate, iterations)
print("Minimum point (x, y):", minimum_point)
print("Minimum value of the function: ", objective_function(*minimum_point))
