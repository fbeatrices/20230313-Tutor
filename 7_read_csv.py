#
# Template for Python program
#
import pandas as pd

# 1. Input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)
print(raw_data.info())

# 2. Process
total = raw_data["Price"].sum()

# 3. Output
print(f"Total: {total}")