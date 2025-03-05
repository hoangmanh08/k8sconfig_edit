# import yaml

# # Đọc nội dung từ file input.yaml
# with open('output1.yaml', 'r') as file:
#     data = yaml.safe_load(file)

# # Hàm để loại bỏ các chỉ số mảng trong cấu trúc YAML
# def remove_array_indices(data):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             data[key] = remove_array_indices(value)
#     elif isinstance(data, list):
#         # Nếu gặp list, chỉ cần trả về một list mới mà không có các chỉ số kiểu mảng
#         return [remove_array_indices(item) for item in data]
#     return data

# # Loại bỏ các chỉ số mảng trong cấu trúc YAML
# cleaned_data = remove_array_indices(data)

# # Ghi lại dữ liệu đã sửa đổi vào file output.yaml
# with open('step_2_output.yaml', 'w') as file:
#     yaml.dump(cleaned_data, file, default_flow_style=False)

# print("Đã loại bỏ các chỉ số mảng và lưu kết quả vào output.yaml.")

import yaml
import re

# Đọc nội dung từ file input.yaml
with open('output1.yaml', 'r') as file:
    data = file.read()

# Sử dụng regex để loại bỏ chỉ số mảng từ các khóa
data_cleaned = re.sub(r'(\w+)\[\d+\]', r'\1', data)

# Ghi lại dữ liệu đã sửa đổi vào file output.yaml
with open('step_2_output.yaml', 'w') as file:
    file.write(data_cleaned)

print("Đã loại bỏ các chỉ số mảng và lưu kết quả vào output.yaml.")

