"""
    This program is designed to show how to use data frames and data manipulation tasks in pandas
"""

import pandas as pd

# data framres

data = {
    "Name": ["John", "Cathy", "Ross", "Jack"], 
    "Age": [28, 47, 36, 51],
    "City": ["Los Angeles", "Chicago", "Miami", "New York"]
}

american = {
    "Name": ["Scott", "Michael", "Marc"],
    "City": ["Pensylvania", "Washinton DC", "California"]
}

american_df = pd.DataFrame(american)

malagasy = {
    "Name": ["Andry", "Fitia", "Tolotra"],
    "City": ["Tana", "Antsirabe", "Toamasina"]
}

malagasy_df = pd.DataFrame(malagasy)

df = pd.DataFrame(data)
print("The date frames")
print(df)

age_series = df["Age"]
print("\n The Age column is extracted:")
print(age_series)

# Data Manipulation Tasks

# filter
adult = df.query("Age>30")
print("\n Filter rows where Age is greater than 30:")
print(adult)

# slicing
last_two_rows = df.iloc[2:4, 0:2]
print("\n Select rows 2 to 3 and columns 0 to 1")
print(last_two_rows)

df.set_index("Name", inplace=True)
two_first_rows = df.loc["John":"Cathy"]
print("\n The two first rows")
print(two_first_rows)

# merging
people = pd.concat([american_df, malagasy_df], keys=['American', 'Malagasy'])
print("\n Concatenate the American and Malagasy data frames:")
print(people)
