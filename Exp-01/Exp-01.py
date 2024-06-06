#Calculating the Euclidean Distance Between Two Points
import numpy as np
def euclidean_distance(p, q):
  return np.sqrt(np.sum((q - p) ** 2))
# Example usage
p = np.array([1, 2])
q = np.array([4, 6])
distance = euclidean_distance(p, q)
print('Output for Calculating the Euclidean Distance Between Two Points is: ',distance)

#Calculating the Dot Product of Two Vectors
import numpy as np
A = np.array([1, 3, -5])
B = np.array([4, -2, -1])
dot_product = np.dot(A, B)
print('Output for dot product of two vectors A and B is ',dot_product)

#Solving a System of Linear Equations
import numpy as np
# Coefficients matrix A and result vector b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
# Solve for x
x = np.linalg.solve(A, b)
print('Output solution of System of Linear Equations is ',x)
