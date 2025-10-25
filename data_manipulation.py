"""
    This program shows how to use other manipulation tasks
"""
import pandas as pd

data = {
    'Name': ["Jhon Doe", "Alex", "Jane", "Katty", "Bob"],
    'Age': [25, 36, 27, 40, 38],
    'City': ["Miami", "LA", "Chicago", "Chicago", "Miami"],
    'Salary': [70000, 80000, 90000, 75000, 95000]
}

df = pd.DataFrame(data)
print(df)

# group by City and calculate the mean for numeric columns
city_data = df.groupby('City').mean(numeric_only=True)
print('\nGrouped by city with the means of numeric data:')
print(city_data)
