import pandas as pd
import numpy as np

data = pd.read_json('data/default-cards-20250616213306.json')

unique_values = {}
for column in ["color_identity", "legalities", "mana_cost", "type_line"]:
    unique_values[column] = data[column].apply(str).unique()

for column, values in unique_values.items():
    print(f"Unique values in column '{column}':")
    print(values)

# np.unique([type.split(' — ')[0] for type in unique_values["type_line"]]) 