
import numpy as np
import matplotlib.pyplot as plt
# Define the sigmoid function 
def sigmoid(x):
  return 1 / (1 + np.exp(-x))
# Define the tanh function
def tanh(x):
  return np.tanh(x)
# Generate a random array of values using numpy
random_values = np.random.randn(10) # Generate 10 random values from a standard normal distribution
# Calculate the sigmoid and tanh (hyperbolic tangent) of these random values
sigmoid_values = sigmoid (random_values)
tanh_values = tanh (random_values)

# Generate indices for x-axis 
indices = np.arange(len(random_values))
# Plotting
plt.figure(figsize=(14, 6))
# Plot for Sigmoid values
plt.subplot(1, 2, 1)
plt.scatter (indices, sigmoid_values, color='blue', label='Sigmoid Values')
plt.plot(indices, sigmoid_values, color='lightblue', linestyle='--')
plt.title('Sigmoid Function')
plt.xlabel('Index')
plt.ylabel('Sigmoid Value')
plt.grid(True)
plt.legend()
# Plot for Tanh values
plt.subplot(1, 2, 2)
plt.scatter(indices, tanh_values, color='red', label='Tanh Values')
plt.plot(indices, tanh_values, color='pink', linestyle='--')
plt.title('Tanh Function')
plt.xlabel('Index')
plt.ylabel('Tanh Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
