# import yaml  
# import toml  
# from collections import OrderedDict  

# # Hàm chuyển đổi file YAML sang TOML với tham số cho phép giữ nguyên thứ tự  
# def yaml_to_toml(yaml_file, toml_file, ordered=True):  
#     # Đọc file YAML  
#     with open(yaml_file, 'r', encoding='utf-8') as yf:  
#         if ordered:  
#             yaml_data = yaml.safe_load(yf)  # Dữ liệu mặc định là dict (không đảm bảo thứ tự)  
#             yaml_data = OrderedDict(yaml_data)  # Chuyển đổi thành OrderedDict để giữ nguyên thứ tự  
#         else:  
#             yaml_data = yaml.safe_load(yf)  

#     # Ghi dữ liệu vào file TOML  
#     with open(toml_file, 'w', encoding='utf-8') as tf:  
#         toml.dump(yaml_data, tf)  


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
        # Mỗi dòng sẽ là một phần tử trong danh sách lines
        lines = toml_output.splitlines()  
        for i in range(len(lines)):  

            flag = False

            #Kiểm tra xem dòng có dạng '[  ]'
            if lines[i].startswith("[[") and "]]" in lines[i]:
                flag = True
                #Tìm vị trí dấu chấm đầu tiên
                start_idx = lines[i].find(".")
                # Nếu có một dấu chấm và nó không phải là ký tự cuối cùng
                if start_idx != -1 and start_idx < len(lines[i]) - 1:
                    # Thêm dấu ngoặc kép sau dấu chấm đầu tiên
                    first_part = lines[i][:start_idx + 1]
                    rest_part = lines[i][start_idx + 1:]
                    
                    # Tìm vị trí của '.cri' hoặc '.v1.cri'
                    cri_idx2 = rest_part.find('.local')
                    
                    if cri_idx2 != -1 and cri_idx2 + 6 < len(rest_part):
                        # Chèn ngoặc kép sau 'cri'
                        before_cri = rest_part[:cri_idx2 + 6]  # Bao gồm '.cri'
                        after_cri = rest_part[cri_idx2 + 6:]   # Phần còn lại sau '.cri'
                        lines[i] = first_part + '"' + before_cri + '"' + after_cri

            if flag:
                if '=' in lines[i]:  # chỉ lùi những dòng có hình dạng key=value  
                    lines[i] = '  ' + lines[i]  
                continue


            #Kiểm tra xem dòng có dạng '[  ]'
            if lines[i].startswith("[") and "]" in lines[i]:
                #Tìm vị trí dấu chấm đầu tiên
                start_idx = lines[i].find(".")
                # Nếu có một dấu chấm và nó không phải là ký tự cuối cùng
                if start_idx != -1 and start_idx < len(lines[i]) - 1:
                    # Thêm dấu ngoặc kép sau dấu chấm đầu tiên
                    first_part = lines[i][:start_idx + 1]
                    rest_part = lines[i][start_idx + 1:]
                    
                    # Tìm vị trí của '.cri' hoặc '.v1.cri'
                    cri_idx = rest_part.find('.cri')
                    cri_idx1 = rest_part.find(']')
                    
                    if cri_idx != -1 and cri_idx + 4 < len(rest_part):
                        # Chèn ngoặc kép sau 'cri'
                        before_cri = rest_part[:cri_idx + 4]  # Bao gồm '.cri'
                        after_cri = rest_part[cri_idx + 4:]   # Phần còn lại sau '.cri'
                        lines[i] = first_part + '"' + before_cri + '"' + after_cri
                    else:
                        # Chèn ngoặc kép sau 'cri'
                        before_cri1 = rest_part[:cri_idx1]  
                        lines[i] = first_part + '"' + before_cri1 + '"' + ']'

                        # # Nếu không tìm thấy '.cri', chỉ thêm dấu ngoặc kép sau dấu chấm đầu tiên
                        # lines[i] = first_part + '"' + rest_part + '"'

            if '=' in lines[i]:  # chỉ lùi những dòng có hình dạng key=value  
                lines[i] = '  ' + lines[i]  

        tf.write("\n".join(lines))  # Ghi lại các dòng đã lùi vào file  


# Đường dẫn đến file YAML và file TOML  
yaml_input = 'main_tom.yaml'  # Thay đổi tên file YAML của bạn tại đây  
toml_output = 'yam_tom_output2.toml'  # Thay đổi tên file TOML của bạn tại đây  

# Thực hiện chuyển đổi  
yaml_to_toml(yaml_input, toml_output)  

print(f"Đã chuyển đổi {yaml_input} thành {toml_output}.")  