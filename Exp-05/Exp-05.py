import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
tf.random.set_seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Create a linear model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,), name='input_layer'),
    tf.keras.layers.Dense(1, name='output_layer')
])

# Compile the model
model.compile(optimizer='sgd', loss='mse')  # sgd stands for Stochastic Gradient Descent

# Display the model summary
model.summary()

# Train the model
history = model.fit(X, y, epochs=100, verbose=0)

# Plot the training loss
plt.plot(history.history['loss'])
plt.title('Model Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Mean Squared Error')
plt.show()

# Get the learned weight and bias
weight, bias = model.layers[1].get_weights()
print("Weight:", weight[0, 0])
print("Bias:", bias[0])

# Make predictions
X_new = np.array([[0], [2]])
predictions = model.predict(X_new)

# Display predictions
for i in range(len(X_new)):
    print(f"Input: {X_new[i][0]}, Predicted Output: {predictions[i][0]}")
