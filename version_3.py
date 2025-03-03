import pandas as pd
import yaml
import os
import re

# Đường dẫn đến file Excel
file_path = "etcd.xlsx" 

# Kiểm tra xem file có tồn tại không
if not os.path.exists(file_path):
    print(f"File {file_path} không tồn tại.")
else:
    try:
        # Đọc file Excel vào DataFrame
        df = pd.read_excel(file_path)

        # Kiểm tra xem các cột cần thiết có trong DataFrame không
        if "Parameter" not in df.columns or "Value" not in df.columns:
            print("File Excel phải chứa các cột 'Parameter' và 'Value'.")
        else:
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

                value = row["Value"]

                if pd.isna(value):  # Bỏ qua các giá trị rỗng
                    continue

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

            # Lưu kết quả vào file YAML
            with open("version_3_output.yaml", "w") as file:
                yaml.dump(yaml_dict, file, default_flow_style=False, sort_keys=False)

            print("YAML file đã được tạo: output1.yaml")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
