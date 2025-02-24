import pandas as pd
import yaml

# Load the Excel file
file_path = "etcd.xlsx"  # Change file name .xlsx
df = pd.read_excel(file_path)

# df = df.replace("v","b", regex=True)
df['Parameter'] = df['Parameter'].str.replace(r'\[\d+\]', '', regex=True) 

yaml_dict = {}  

# df.to_csv("df.csv", index = True)

# for _, row in df.iterrows():  
#     keys = row["Parameter"].split(".")  
#     value = row["Value"]  

#     if pd.isna(value):  # Bỏ qua nếu giá trị trống  
#         continue  

#     # Tạm thời  
#     temp = yaml_dict  

#     for key in keys[:-1]:  # Điều hướng tới cấp độ lồng nhau cuối cùng  
#         key = key.replace(']', '').replace('[', '.')  # Xử lý chỉ số (thay thế dấu [] bằng .)  
#         temp = temp.setdefault(key, {})  
        
#     # Gán giá trị cho khóa cuối  
#     last_key = keys[-1].replace(']', '').replace('[', '.')  # Đảm bảo khóa cuối không có dấu [] trong  
#     if last_key not in temp:  
#         temp[last_key] = []  
        
#     temp[last_key].append(value)  # Thêm giá trị vào danh sách

a = 0
list_a = []

for _, row in df.iterrows():
    keys = row["Parameter"].split(".")  # Split keys by "."
    value = row["Value"]

    # if pd.isna(value):  # Skip empty values
    #     continue

    # Build the nested dictionary dynamically
    temp = yaml_dict
    for key in keys[:-1]:  # Traverse to the last nested level
        temp = temp.setdefault(key, {})

    if a == 0:
        a = keys[-1]
        list_a.append(value)

    if len(list_a) > 1:
        temp[keys[-1]] = list_a  # Assign the final value

print(list_a)

# Save to a YAML file
# with open("version_2_output.yaml", "w") as file:
#     yaml.dump(yaml_dict, file, default_flow_style=False, sort_keys=False)

# print("YAML file created: output.yaml")