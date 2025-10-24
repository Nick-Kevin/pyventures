"""
    This program is designed to show to use data frames in pandas
"""

import pandas as pd

dataFrames = {
    "Name": ["John", "Cathy", "Ross", "Jack"], 
    "Age": [28, 47, 36, 51],
    "City": ["Los Angeles", "Chicago", "Miami", "New York"]
}

df = pd.DataFrame(dataFrames)

print("The date frames")
print(df)

age_series = df["Age"]

print("\n The Age column is extracted:")
print(age_series)
