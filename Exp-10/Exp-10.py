import pandas as pd

# Creating car selling data
car_selling_data = {
    'Brand': ['Maruti', 'Maruti', 'Maruti', 'Maruti', 'Hyundai', 'Hyundai', 'Toyota', 'Mahindra', 'Mahindra', 'Ford', 'Toyota', 'Ford'],
    'Year': [2010, 2011, 2009, 2013, 2010, 2011, 2011, 2010, 2013, 2010, 2010, 2011],
    'Sold': [6, 7, 9, 8, 3, 5, 2, 8, 7, 2, 4, 2]
}

# Creating DataFrame for car selling data
df_car = pd.DataFrame(car_selling_data)

print("\nOriginal Car Selling DataFrame:\n", df_car)

# Grouping the car data by year
grouped_car = df_car.groupby("Year")

print("\nGroup by year 2010:\n", grouped_car.get_group(2010))

# Student data
student_data = {
    'Name': ['Amit', 'Praveen', 'Jagadesh', 'Rahul', 'Vishal', 'Suraj', 'Rishab', 'Sathish', 'Amit', 'Rahul', 'Praveen', 'Amit'],
    'Roll no': [123, 54, 29, 36, 59, 38, 12, 45, 34, 36, 54, 23],
    'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com', 'xxxxxx@gmail.com', 'xx@gmail.com', 'xxxxx@gmail.com', 'xxxxx@gmail.com', 'xxxx@gmail.com', 'xxxxx@gmail.com', 'xxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']
}

# Creating DataFrame for student data
df_student = pd.DataFrame(student_data)

print("\nOriginal Student DataFrame:\n", df_student)

# Removing duplicate rows based on 'Roll no'
non_duplicate_student = df_student[~df_student.duplicated('Roll no')]

# Printing non-duplicate values
print("\nRemoved duplicated rows:\n", non_duplicate_student)

# Details DataFrame
details = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'NAME': ['Arun', 'Praveen', 'Harish', 'Pooja', 'Rahul', 'Naresh', 'Saurabh', 'Anush', 'Dinesh', 'Mohit'],
    'BRANCH': ['Mech', 'Mech', 'CSE', 'CSE', 'CSE', 'EEE', 'EEE', 'ECE', 'ECE', 'IT']
})

print("\nOriginal Details DataFrame:\n", details)

# Fees status DataFrame
fees_status = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'PENDING': ['5000', '250', 'NIL', '9000', '15000', 'NIL', '4500', '1800', '250', 'NIL']
})

print("\nOriginal Fees Status DataFrame:\n", fees_status)

# Merging DataFrames
merged_df = pd.merge(details, fees_status, on='ID')
print("\nMerged DataFrame:\n", merged_df)
