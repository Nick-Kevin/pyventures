import pandas as pd

dataFrames = {
    "Name": ["John", "Cathy", "Ross", "Jack"], 
    "Age": [28, 47, 36, 51],
    "City": ["Los Angeles", "Chicago", "Miami", "New York"]
}

df = pd.DataFrame(dataFrames)

print(df)