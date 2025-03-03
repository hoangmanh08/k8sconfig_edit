# import pandas as pd
# import yaml

# # Load the Excel file
# file_path = "etcd.xlsx"  # Thay đổi tên file nếu cần
# df = pd.read_excel(file_path)

# # Convert the DataFrame to a dictionary
# yaml_dict = {}

# for _, row in df.iterrows():
#     keys = row["Parameter"].split(".")  # Chia khóa thành danh sách
#     value = row["Value"]

#     # if pd.isna(value):  # Bỏ qua các giá trị trống
#     #     continue

#     # Xây dựng từ điển phân cấp
#     temp = yaml_dict
#     for key in keys[:-1]:  # Duyệt đến cấp cuối cùng
#         # Nếu key chứa dấu ngoặc vuông (mảng), cần tạo mảng (list) thay vì dict
#         if "[" in key and "]" in key:
#             key_name = key.split("[")[0]  # Lấy phần tên trước dấu ngoặc vuông
#             try:
#                 index = int(key.split("[")[1].replace("]", ""))  # Lấy chỉ số mảng
#                 # Nếu chưa có mảng, tạo mới
#                 if key_name not in temp:
#                     temp[key_name] = []
#                 # Nếu mảng chưa có đủ phần tử, thêm phần tử trống
#                 while len(temp[key_name]) <= index:
#                     temp[key_name].append(None)
#                 temp[key_name][index] = value  # Gán giá trị vào mảng
#             except (IndexError, ValueError) as e:
#                 # Nếu có lỗi khi xử lý mảng, bỏ qua phần tử hoặc xử lý khác
#                 temp = temp.setdefault(key, {})
#         else:
#             # Nếu không phải là mảng, xử lý như từ điển bình thường
#             temp = temp.setdefault(key, {})

#     # Gán giá trị vào khóa cuối cùng
#     if "[" in keys[-1] and "]" in keys[-1]:  # Nếu là phần tử mảng
#         final_key = keys[-1].split("[")[0]
#         try:
#             index = int(keys[-1].split("[")[1].replace("]", ""))
#             # Gán giá trị vào mảng tương ứng
#             if final_key not in temp:
#                 temp[final_key] = []
#             while len(temp[final_key]) <= index:
#                 temp[final_key].append(None)  # Đảm bảo mảng có đủ phần tử
#             temp[final_key][index] = value
#         except (IndexError, ValueError):
#             # Nếu có lỗi khi xử lý mảng, bỏ qua hoặc xử lý khác
#             temp[final_key] = value
#     else:
#         temp[keys[-1]] = value  # Gán giá trị vào từ điển cuối cùng

# # Lưu cấu trúc YAML vào file
# with open("version_2_output.yaml", "w") as file:
#     yaml.dump(yaml_dict, file, default_flow_style=False, sort_keys=False)

# print("YAML file created: output.yaml")

# import pandas as pd
# import yaml

# # Load the Excel file
# file_path = "etcd.xlsx"  # Thay đổi tên file nếu cần
# df = pd.read_excel(file_path)

# # Convert the DataFrame to a dictionary
# yaml_dict = {}

# for _, row in df.iterrows():
#     keys = row["Parameter"].split(".")  # Chia khóa thành danh sách
#     value = row["Value"]

#     if pd.isna(value):  # Bỏ qua các giá trị trống
#         continue

#     # Xây dựng từ điển phân cấp
#     temp = yaml_dict
#     for key in keys[:-1]:  # Duyệt đến cấp cuối cùng
#         # Nếu key chứa dấu ngoặc vuông (mảng), cần tạo mảng (list) thay vì dict
#         if "[" in key and "]" in key:
#             key_name = key.split("[")[0]  # Lấy phần tên trước dấu ngoặc vuông
#             try:
#                 index = int(key.split("[")[1].replace("]", ""))  # Lấy chỉ số mảng
#                 # Nếu chưa có mảng, tạo mới
#                 if key_name not in temp:
#                     temp[key_name] = []
#                 # Nếu mảng chưa có đủ phần tử, thêm phần tử mới
#                 while len(temp[key_name]) <= index:
#                     temp[key_name].append({})
#                 temp[key_name][index] = temp[key_name][index] or {}  # Khởi tạo phần tử nếu chưa có
#             except (IndexError, ValueError) as e:
#                 # Nếu có lỗi khi xử lý mảng, bỏ qua phần tử hoặc xử lý khác
#                 temp = temp.setdefault(key, {})
#         else:
#             temp = temp.setdefault(key, {})

#     # Gán giá trị vào khóa cuối cùng
#     if "[" in keys[-1] and "]" in keys[-1]:  # Nếu là phần tử mảng
#         final_key = keys[-1].split("[")[0]
#         try:
#             index = int(keys[-1].split("[")[1].replace("]", ""))
#             # Gán giá trị vào mảng tương ứng
#             if final_key not in temp:
#                 temp[final_key] = []
#             while len(temp[final_key]) <= index:
#                 temp[final_key].append(None)  # Đảm bảo mảng có đủ phần tử
#             temp[final_key][index] = value
#         except (IndexError, ValueError):
#             # Nếu có lỗi khi xử lý mảng, bỏ qua hoặc xử lý khác
#             temp[final_key] = value
#     else:
#         # Gán giá trị vào cuối cùng của container -> command
#         if "containers" in keys:
#             container_index = int(keys[1].replace("containers[", "").replace("]", ""))
#             if "command" in keys[-1]:
#                 temp["containers"][container_index]["command"] = temp["containers"][container_index].get("command", [])
#                 temp["containers"][container_index]["command"].append(value)
#         else:
#             temp[keys[-1]] = value

# # Lưu cấu trúc YAML vào file
# with open("version_2_output.yaml", "w") as file:
#     yaml.dump(yaml_dict, file, default_flow_style=False, sort_keys=False)

# print("YAML file created: output.yaml")

# import pandas as pd
# import yaml

# # Load the Excel file
# file_path = "etcd.xlsx"  # Thay đổi tên file nếu cần
# df = pd.read_excel(file_path)

# # Convert the DataFrame to a dictionary
# yaml_dict = {}

# for _, row in df.iterrows():
#     keys = row["Parameter"].split(".")  # Chia khóa thành danh sách
#     value = row["Value"]

#     if pd.isna(value):  # Bỏ qua các giá trị trống
#         continue

#     # Xây dựng từ điển phân cấp
#     temp = yaml_dict
#     for key in keys[:-1]:  # Duyệt đến cấp cuối cùng
#         # Nếu key chứa dấu ngoặc vuông (mảng), cần tạo mảng (list) thay vì dict
#         if "[" in key and "]" in key:
#             key_name = key.split("[")[0]  # Lấy phần tên trước dấu ngoặc vuông
#             try:
#                 index = int(key.split("[")[1].replace("]", ""))  # Lấy chỉ số mảng
#                 # Nếu chưa có mảng, tạo mới
#                 if key_name not in temp:
#                     temp[key_name] = []
#                 # Nếu mảng chưa có đủ phần tử, thêm phần tử mới
#                 while len(temp[key_name]) <= index:
#                     temp[key_name].append({})
#                 temp[key_name][index] = temp[key_name][index] or {}  # Khởi tạo phần tử nếu chưa có
#             except (IndexError, ValueError) as e:
#                 # Nếu có lỗi khi xử lý mảng, bỏ qua phần tử hoặc xử lý khác
#                 temp = temp.setdefault(key, {})
#         else:
#             temp = temp.setdefault(key, {})

#     # Gán giá trị vào khóa cuối cùng
#     if "[" in keys[-1] and "]" in keys[-1]:  # Nếu là phần tử mảng
#         final_key = keys[-1].split("[")[0]
#         try:
#             index = int(keys[-1].split("[")[1].replace("]", ""))
#             # Gán giá trị vào mảng tương ứng
#             if final_key not in temp:
#                 temp[final_key] = []
#             while len(temp[final_key]) <= index:
#                 temp[final_key].append(None)  # Đảm bảo mảng có đủ phần tử
#             temp[final_key][index] = value
#         except (IndexError, ValueError):
#             # Nếu có lỗi khi xử lý mảng, bỏ qua hoặc xử lý khác
#             temp[final_key] = value
#     else:
#         # Gán giá trị vào phần tử cuối cùng
#         temp[keys[-1]] = value

# # Lưu cấu trúc YAML vào file
# with open("version-2_output.yaml", "w") as file:
#     yaml.dump(yaml_dict, file, default_flow_style=False, sort_keys=False)

# print("YAML file created: output.yaml")


import pandas as pd
import yaml

# Load the Excel file
file_path = "etcd.xlsx"  # Thay đổi tên file nếu cần
df = pd.read_excel(file_path)

# Convert the DataFrame to a dictionary
yaml_dict = {}

# Hàm để loại bỏ các mảng hoặc từ điển trống
def remove_empty_elements(d):
    if isinstance(d, list):
        # Xóa các phần tử rỗng trong list
        d[:] = [x for x in d if x]  # Giữ lại các phần tử không rỗng
    elif isinstance(d, dict):
        # Duyệt qua từng phần tử trong dict
        for key, value in list(d.items()):
            remove_empty_elements(value)
            # Xóa các phần tử trong dict nếu chúng rỗng
            if isinstance(value, (dict, list)) and not value:
                del d[key]

# Xử lý dữ liệu từ dataframe
for _, row in df.iterrows():
    keys = row["Parameter"].split(".")  # Chia khóa thành danh sách
    value = row["Value"]

    if pd.isna(value):  # Bỏ qua các giá trị trống
        continue

    # Xây dựng từ điển phân cấp
    temp = yaml_dict
    for key in keys[:-1]:  # Duyệt đến cấp cuối cùng
        if "[" in key and "]" in key:  # Nếu là phần tử mảng
            key_name = key.split("[")[0]  # Lấy phần tên trước dấu ngoặc vuông
            try:
                index = int(key.split("[")[1].replace("]", ""))  # Lấy chỉ số mảng
                if key_name not in temp:
                    temp[key_name] = []
                while len(temp[key_name]) <= index:
                    temp[key_name].append({})
                temp[key_name][index] = temp[key_name][index] or {}  # Khởi tạo phần tử nếu chưa có
            except (IndexError, ValueError):
                temp = temp.setdefault(key, {})
        else:
            temp = temp.setdefault(key, {})

    # Gán giá trị vào khóa cuối cùng
    if "[" in keys[-1] and "]" in keys[-1]:  # Nếu là phần tử mảng
        final_key = keys[-1].split("[")[0]
        try:
            index = int(keys[-1].split("[")[1].replace("]", ""))
            if final_key not in temp:
                temp[final_key] = []
            while len(temp[final_key]) <= index:
                temp[final_key].append(None)  # Đảm bảo mảng có đủ phần tử
            temp[final_key][index] = value
        except (IndexError, ValueError):
            temp[final_key] = value
    else:
        # Gán giá trị vào phần tử cuối cùng
        temp[keys[-1]] = value

# Loại bỏ các mảng hoặc từ điển trống sau khi xây dựng cấu trúc
remove_empty_elements(yaml_dict)

# Lưu cấu trúc YAML vào file
with open("version_4_output.yaml", "w") as file:
    yaml.dump(yaml_dict, file, default_flow_style=False)

print("YAML file created: output.yaml")


