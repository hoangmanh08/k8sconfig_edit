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

            # Duyệt qua từng dòng trong DataFrame
            for _, row in df.iterrows():
                keys = row["Parameter"]

                # Loại bỏ phần chỉ số mảng [0], [1], ... bằng regex
                keys = re.sub(r"\[\d*\]", "", keys)

                # Tách khóa theo dấu "."
                keys = keys.split(".")

                value = row["Value"]

                if pd.isna(value):  # Bỏ qua các giá trị rỗng
                    continue

                # Duyệt qua cấu trúc lồng nhau của từ điển YAML
                temp = yaml_dict
                for key in keys[:-1]:  # Duyệt đến cấp cuối cùng của dictionary
                    temp = temp.setdefault(key, {})

                final_key = keys[-1]

                # Kiểm tra xem khóa cuối cùng có phải là mảng hay không
                if final_key in temp:
                    # Nếu giá trị đã tồn tại và là một chuỗi, chuyển thành danh sách
                    if isinstance(temp[final_key], str):
                        temp[final_key] = [temp[final_key]]
                    # Thêm giá trị mới vào danh sách
                    temp[final_key].append(value)
                else:
                    # Nếu chưa có giá trị, gán trực tiếp
                    temp[final_key] = value

            # Điều chỉnh để xử lý các trường hợp như không phụ thuộc vào tên khóa cụ thể
            def adjust_single_value_lists(d):
                for key, value in d.items():
                    if isinstance(value, dict):
                        adjust_single_value_lists(value)
                    elif isinstance(value, list) and len(value) == 1:
                        # Nếu mảng chỉ có một phần tử, chuyển nó thành giá trị đơn
                        d[key] = value[0]
                    elif isinstance(value, list):
                        # Kiểm tra trường hợp có nhiều giá trị thì giữ nguyên mảng
                        pass

            # Chỉnh sửa yaml_dict để loại bỏ mảng khi không cần thiết
            adjust_single_value_lists(yaml_dict)

            # Lưu kết quả vào file YAML
            output_file = "version_4_output.yaml"
            with open(output_file, "w") as file:
                yaml.dump(yaml_dict, file, default_flow_style=False, sort_keys=False)

            print(f"YAML file đã được tạo: {output_file}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
