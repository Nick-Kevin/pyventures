"""
    This program shows how to use other manipulation tasks
"""
import pandas as pd

data = {
    'Name': ["Jhon Doe", "Alex", "Jane", "Katty", "Bob"],
    'Age': [25, 36, 27, 40, 38],
    'City': ["Miami", "LA", "Chicago", "Chicago", "Miami"],
    'Basic salary': [70000, 80000, 90000, 75000, 95000],
    'Allowance': [1000, 2500, 700, 1500, 1750]
}

df = pd.DataFrame(data)
print(df)

# group by City and calculate the mean for numeric columns
city_data = df.groupby('City').mean(numeric_only=True)
print('\nGrouped by city with the means of numeric data:')
print(city_data)

city_elaborated = df.groupby('City').agg({
    'Age': ['mean', 'min', 'max'],
    'Basic salary': ['sum', 'mean']
})
print('\nThe city data with more operations:')
print(city_elaborated)

# sorting
ascending_ages = df.sort_values('Age')
print('\nData sorted by ages:\n', ascending_ages)

# transoforming
df['Gross salary'] = df['Basic salary'] + df['Allowance']
print('\nData with gross salary:\n', df)
