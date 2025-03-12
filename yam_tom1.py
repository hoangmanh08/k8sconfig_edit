import yaml  
import tomlkit  

# Hàm chuyển đổi file YAML sang TOML  
def yaml_to_toml(yaml_file, toml_file):  
    # Đọc file YAML  
    with open(yaml_file, 'r', encoding='utf-8') as yf:  
        yaml_data = yaml.safe_load(yf)  

    # Tạo một tài liệu TOML mới  
    toml_data = tomlkit.document()  

    # Đưa dữ liệu từ YAML vào TOML đồng thời giữ nguyên thứ tự  
    for key, value in yaml_data.items():  
        toml_data[key] = value  

    # Ghi dữ liệu vào file TOML  
    with open(toml_file, 'w', encoding='utf-8') as tf:  
        # tf.write(tomlkit.dumps(toml_data))  
        toml_output = tomlkit.dumps(toml_data)  

        # Thêm lùi đầu dòng cho mỗi dòng giá trị trong bản thân chuỗi đầu ra  
        lines = toml_output.splitlines()  
        for i in range(len(lines)):  
            if '=' in lines[i]:  # chỉ lùi những dòng có hình dạng key=value  
                lines[i] = '  ' + lines[i]  

        tf.write("\n".join(lines))  # Ghi lại các dòng đã lùi vào file  


# Đường dẫn đến file YAML và file TOML  
yaml_input = 'main_tom.yaml'  # Thay đổi tên file YAML của bạn tại đây  
toml_output = 'yam_tom_output1.toml'  # Thay đổi tên file TOML của bạn tại đây  

# Thực hiện chuyển đổi  
yaml_to_toml(yaml_input, toml_output)  

print(f"Đã chuyển đổi {yaml_input} thành {toml_output}.")  