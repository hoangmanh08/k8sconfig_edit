import pandas as pd
import toml
import os
import re

# Đường dẫn đến file Excel
file_path = "config.toml.xlsx" 

# Hàm encoder tùy chỉnh
def custom_encoder(obj):
    # Giả sử bạn muốn xử lý các kiểu dữ liệu đặc biệt, bạn có thể thêm logic vào đây.
    # Trong trường hợp này, chúng ta không cần xử lý thêm, vì dữ liệu TOML đơn giản.
    if isinstance(obj, dict):
        # Nếu đối tượng là dictionary, trả về một định dạng TOML có các tables
        return obj
    raise TypeError(f"Type {type(obj)} not serializable")

# Đọc file Excel vào DataFrame
df = pd.read_excel(file_path)

# Kiểm tra xem các cột cần thiết có trong DataFrame không
if "Parameter" not in df.columns or "Setup Value" not in df.columns:
    print("File Excel phải chứa các cột 'Parameter' và 'Value'.")
# Chuyển đổi DataFrame thành dictionary YAML
yaml_dict = {}

# Tạo một từ điển để lưu trữ các giá trị của các trường có thể có nhiều giá trị
command_dict = {}

for _, row in df.iterrows():
    keys = row["Parameter"]

    # Loại bỏ phần chỉ số mảng [0], [1], ... bằng regex
    keys = re.sub(r"\[\d*\]", "", keys)

    # Tách khóa theo dấu "."
    keys = keys.split(".")

    value = row["Setup Value"]

    if pd.isna(value):  # Bỏ qua các giá trị rỗng
        value =""

    # Tạo từ điển lồng nhau
    temp = yaml_dict
    for key in keys[:-1]:  # Duyệt đến cấp cuối cùng của dictionary
        temp = temp.setdefault(key, {})

    final_key = keys[-1]

    # Nếu có nhiều dòng có cùng khóa (ví dụ: command), cần lưu giá trị dưới dạng mảng
    if final_key in temp:
        # Nếu giá trị là một chuỗi, chuyển thành danh sách
        if isinstance(temp[final_key], str):
            temp[final_key] = [temp[final_key]]
        # Thêm giá trị mới vào danh sách
        temp[final_key].append(value)
    else:
        # Nếu chưa có giá trị, gán trực tiếp
        temp[final_key] = value

# Hàm custom_encoder - không thay đổi gì trong dữ liệu này
# (bạn có thể tùy chỉnh nếu cần nhưng trong trường hợp này không cần thiết)
def custom_encoder(value):
    # Ở đây có thể thực hiện các xử lý tùy chỉnh nếu cần, ví dụ:
    # Chuyển kiểu dữ liệu float thành chuỗi hoặc các kiểu đặc biệt khác
    if isinstance(value, float):
        return str(value)  # Chuyển đổi giá trị float thành chuỗi
    return value

# Hàm để áp dụng custom_encoder
def apply_custom_encoder(data, encoder):
    if isinstance(data, dict):
        return {key: apply_custom_encoder(value, encoder) for key, value in data.items()}
    elif isinstance(data, list):
        return [apply_custom_encoder(item, encoder) for item in data]
    else:
        return encoder(data)  # Áp dụng encoder cho giá trị

# Áp dụng custom_encoder trước khi ghi vào TOML
encoded_data = apply_custom_encoder(yaml_dict, custom_encoder)


# Lưu kết quả vào file TOML
with open("output_test_1.toml", "w") as file:
    toml.dump(encoded_data, file)

print("TOML file đã được tạo: output1.yaml")
