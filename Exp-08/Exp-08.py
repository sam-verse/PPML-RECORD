import numpy as np

arr1 = [10, 20, 30, 40, 50]
arr2 = [2, 4, 5, 8, 10]

a = np.array(arr1)
b = np.array(arr2)

print("Original arrays:")
print(a)
print(b)

print("\nVector addition:")
print(a + b)

print("\nVector subtraction:")
print(a - b)

print("\nVector multiplication:")
print(a * b)

print("\nVector division:")
print(a / b)

print("\nVector Dot product:")
print(np.dot(a, b))

print("\nScalar multiplication:")
sclr = 5
print("Scalar value =", sclr)
print("Array =", a)
print("Result =", a * sclr)

# Numpy.Vectorize method
def my_func(x, y):
    # "Return x-y if x>y, otherwise return x+y"
    if x > y:
        return x - y
    else:
        return x + y

print("\n\nNumpy.Vectorize method")
print("(Return x-y if x>y, otherwise return x+y)")

arr1 = [10, 4, 20]
arr2 = [2, 3, 30]
vec_func = np.vectorize(my_func)

print("Array1:", arr1)
print("Array2:", arr2)
print("Result:", vec_func(arr1, arr2))
