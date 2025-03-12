import pandas as pd
import yaml

# Load the Excel file
file_path = "etcd_edit.xlsx"  # Change file name .xlsx
df = pd.read_excel(file_path)

# Convert the DataFrame to a dictionary
yaml_dict = {}

for _, row in df.iterrows():
    keys = row["Parameter"].split(".")  # Split keys by "."
    value = row["Value"]

    if pd.isna(value):  # Skip empty values
        continue

    # Build the nested dictionary dynamically
    temp = yaml_dict
    for key in keys[:-1]:  # Traverse to the last nested level
        temp = temp.setdefault(key, {})
    temp[keys[-1]] = value  # Assign the final value

# Save to a YAML file
with open("output_edit.yaml", "w") as file:
    yaml.dump(yaml_dict, file, default_flow_style=False, sort_keys=False)

print("YAML file created: output.yaml")
