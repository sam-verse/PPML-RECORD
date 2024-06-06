import pandas as pd 
import numpy as np

# Creating a hypothetical dataset
data = {
    'Make': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan'],
    'Model': ['Camry', 'Civic', 'Fusion', 'Malibu', 'Altima'],
    'Fuel_Efficiency_MPG': [28, 36, 30, 32, 26],
    'Engine_Power_HP': [203, 158, 181, 163, 188],
    'Acceleration_0_60mph_s': [7.5, 8.2, 6.9, 8.0, 6.2],
    'Weight_kg': [1500, 1300, 1400, 1350, 1550]
}
car_performance_df = pd.DataFrame(data)

# Task 1: Correlation Analysis
correlation_matrix = car_performance_df[['Fuel_Efficiency_MPG', 'Engine_Power_HP', 'Acceleration_0_60mph_s', 'Weight_kg']].corr()

# Task 2: Performance Index Calculation
car_performance_df['Performance_Index'] = (
    0.4 * car_performance_df['Fuel_Efficiency_MPG'] +
    0.4 * car_performance_df['Engine_Power_HP'] -
    0.2 * car_performance_df['Acceleration_0_60mph_s']
)

# Task 3: Top Performing Cars
top_performing_cars = car_performance_df.nlargest(2, 'Performance_Index')

# Task 4: Weight Adjustment (Min-Max scaling)
min_max_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
car_performance_df['Weight_normalized'] = car_performance_df[['Weight_kg']].apply(min_max_scaler)

# Output
print("Correlation Matrix:")
print(correlation_matrix)

print("\nDataFrame with Performance Index:")
print(car_performance_df[['Make', 'Model', 'Performance_Index']])

print("\nTop Performing Cars:")
print(top_performing_cars[['Make', 'Model', 'Performance_Index']])

print("\nDataFrame with Weight Adjustment:")
print(car_performance_df[['Make', 'Model', 'Weight_kg', 'Weight_normalized']])



