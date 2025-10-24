"""
    This program is designed to show to use data frames in pandas
"""

import pandas as pd

# data framres

data = {
    "Name": ["John", "Cathy", "Ross", "Jack"], 
    "Age": [28, 47, 36, 51],
    "City": ["Los Angeles", "Chicago", "Miami", "New York"]
}

df = pd.DataFrame(data)
print("The date frames")
print(df)

age_series = df["Age"]
print("\n The Age column is extracted:")
print(age_series)

# Data Manipulation Tasks

adult = df[age_series>30]
print("\n Filter rows where Age is greater than 30:")
print(adult)
