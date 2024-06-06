import pandas as pd

# 1) Create an empty DataFrame
df = pd.DataFrame()

print("Empty DataFrame:")
print(df)

# 2) Declare and print the DataFrame series
# Creating Series
names = pd.Series(['Parker', 'John', 'Smith', 'William'])
ids = pd.Series([102, 107, 109, 114])

# Creating DataFrame
frame = {"Emp": names, "ID": ids}
result = pd.DataFrame(frame)

print("\nDataFrame:")
print(result)

# 3) Add and delete columns
# Adding a new column 'Age'
result['Age'] = pd.Series([35, 24, 40, 38])
print("\nAdding new column:")
print(result)

# Deleting the 'Age' column
result.drop(columns=['Age'], inplace=True)
print("\nDeleting one column:")
print(result)

# 4) Extract, slice, add, and delete rows
# Extracting the third row
print("\nExtracting the third row:")
print(result.loc[2])

# Slicing rows
print("\nSlice rows:\n", result[1:3])

# 5) Adding new row values
# Creating another DataFrame for adding new rows
d2 = pd.DataFrame([['Dale', 123], ['Mark', 143]], columns=['Emp', 'ID'])

# Appending new rows
result = pd.concat([result, d2], ignore_index=True)
print("\nAdding new row values:\n", result)

# 6) Deleting a particular row
# Here we will delete the row with index 1
result = result.drop(index=1)
print("\nDeleting particular row:\n", result)
