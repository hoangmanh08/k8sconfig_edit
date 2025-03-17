import toml
import pandas as pd

# Hàm đọc file toml và chuyển thành dictionary
def read_toml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return toml.load(f)

# Hàm lấy giá trị cuối cùng trong các key-value (đối với dict lồng nhau và mảng)
def extract_final_values(toml_data):
    data_list = []
    
    def recurse_dict(d, parent_key=''):
        # Duyệt qua từng mục trong dictionary
        for key, value in d.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):
                recurse_dict(value, full_key)  # Nếu là dict thì tiếp tục đệ quy
            elif isinstance(value, list):
                # Nếu là list, xử lý từng phần tử của list
                for i, item in enumerate(value):
                    # Tạo key dạng key[index]
                    data_list.append([f"{full_key}[{i}]", item])
            else:
                data_list.append([full_key, value])  # Nếu là giá trị cuối cùng thì thêm vào

    recurse_dict(toml_data)
    return data_list

# Hàm chuyển dữ liệu từ toml sang hàng dọc trong Excel
def toml_to_vertical_excel(toml_file, excel_file):
    # Đọc dữ liệu từ file toml
    toml_data = read_toml(toml_file)
    
    # Lấy danh sách các giá trị cuối cùng từ dữ liệu TOML
    final_values = extract_final_values(toml_data)
    
    # Tạo DataFrame từ data_list
    df = pd.DataFrame(final_values, columns=['Key', 'Value'])
    
    # Xử lý các giá trị TRUE/FALSE và float -> int trong DataFrame
    for index, row in df.iterrows():
        value = row["Value"]

        if isinstance(value, str) and value.upper() == "TRUE":  
            df.at[index, "Value"] = "true"  # Cập nhật giá trị vào DataFrame
        elif isinstance(value, str) and value.upper() == "FALSE":  
            df.at[index, "Value"] = "false"  # Cập nhật giá trị vào DataFrame
        elif isinstance(value, float) and value.is_integer():  
            df.at[index, "Value"] = int(value)  # Cập nhật giá trị vào DataFrame
    
    # Lưu DataFrame vào file Excel (theo kiểu hàng dọc)
    df.to_excel(excel_file, index=False, engine='openpyxl')

# Đường dẫn đến file toml và file excel đầu ra
toml_file = '/workspaces/k8sconfig_edit/tom_edit/config.toml'
excel_file = 'outputtttttt.xlsx'

# Chuyển đổi file
toml_to_vertical_excel(toml_file, excel_file)

print(f"Đã chuyển đổi file {toml_file} thành {excel_file}")


#### LỎ ######