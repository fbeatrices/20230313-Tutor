import pandas as pd

# 1.Input
raw_data = pd.read_csv("readcsv_assignment.csv")
print(raw_data)

# 2. Process
Numberofitems = len(raw_data)
Sorted_data = raw_data.sort_values ("Menu",ascending=True)

# 3. Output
print(f"Count:{Numberofitems}")
print(f'{Sorted_data}')