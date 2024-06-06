import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate some random data for a linear regression problem
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Convert data to TensorFlow tensors
X_tensor = tf.constant(X, dtype=tf.float32)
y_tensor = tf.constant(y, dtype=tf.float32)

# Initialize variables (weights and bias)
W = tf.Variable(tf.random.normal(shape=(1, 1), mean=0.0, stddev=1.0), trainable=True)
b = tf.Variable(tf.zeros(shape=(1,)), trainable=True)

# Define the linear regression model
def linear_regression(x):
    return tf.matmul(x, W) + b

# Define the mean squared error loss function
def mean_squared_error(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# Set hyperparameters
learning_rate = 0.01
num_epochs = 100

# Optimization using gradient descent
for epoch in range(num_epochs):
    with tf.GradientTape() as tape:
        predictions = linear_regression(X_tensor)
        loss = mean_squared_error(y_tensor, predictions)
    
    # Calculate gradients
    gradients = tape.gradient(loss, [W, b])
    
    # Update weights and bias using gradient descent
    W.assign_sub(learning_rate * gradients[0])
    b.assign_sub(learning_rate * gradients[1])
    
    # Print the loss every 10 epochs
    if (epoch + 1) % 10 == 0:
        print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {loss.numpy()}')

# Plot the data points and the linear regression line
plt.scatter(X, y, label='Data points')
plt.plot(X, linear_regression(X_tensor).numpy(), color='red', label='Linear regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
