import pandas as pd
import yaml
import os
import re

# Đường dẫn đến file Excel
file_path = "etcd_sum.xlsx"

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

            # Duyệt qua các dòng trong DataFrame để xây dựng từ điển YAML
            for _, row in df.iterrows():
                keys = row["Parameter"]

                # Loại bỏ chỉ số mảng [0], [1], ... bằng regex
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

                # Nếu có nhiều dòng có cùng khóa, cần lưu giá trị dưới dạng mảng
                if final_key in temp:
                    # Nếu giá trị là một chuỗi, chuyển thành danh sách
                    if isinstance(temp[final_key], str):
                        temp[final_key] = [temp[final_key]]
                    # Thêm giá trị mới vào danh sách
                    temp[final_key].append(value)
                else:
                    # Nếu chưa có giá trị, gán trực tiếp
                    temp[final_key] = value

            # Duyệt qua các khóa có thể là mảng (như 'volumes') để tách các phần tử đúng
            def process_nested_lists(data):
                """ Hàm giúp xử lý các phần tử lồng nhau (nested lists) trong dữ liệu """
                if isinstance(data, dict):
                    for key, value in data.items():
                        # Nếu giá trị là danh sách, kiểm tra mỗi phần tử
                        if isinstance(value, list):
                            # Kiểm tra nếu các phần tử trong danh sách đều là dict, để xử lý các phần tử như 'path', 'type'
                            for item in value:
                                if isinstance(item, dict):
                                    for sub_key, sub_value in item.items():
                                        if isinstance(sub_value, list):
                                            # Đảm bảo giá trị là một mảng
                                            item[sub_key] = [sub_value] if not isinstance(sub_value, list) else sub_value
                        process_nested_lists(value)
                elif isinstance(data, list):
                    for item in data:
                        process_nested_lists(item)

            # Xử lý các trường hợp có mảng trong YAML (nested lists)
            process_nested_lists(yaml_dict)

            # Lưu kết quả vào file YAML
            with open("ttt.yaml", "w") as file:
                yaml.dump(yaml_dict, file, default_flow_style=False, sort_keys=False)

            print("YAML file đã được tạo: ttt.yaml")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
