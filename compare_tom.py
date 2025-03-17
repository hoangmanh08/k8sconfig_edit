import toml

def load_toml_with_lines(file_path):
    """Đọc file TOML và trả về đối tượng Python, đồng thời lưu vị trí dòng."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Chuyển nội dung file thành object Python bằng cách ghép lại các dòng
    content = toml.loads("".join(lines))
    return content, lines

def compare_dicts(dict1, dict2, path="", lines1=None, lines2=None, line_num=0):
    """So sánh hai dictionary và in ra sự khác biệt, bao gồm dòng số."""
    if dict1 == dict2:
        return []

    differences = []

    # Kiểm tra các key có mặt trong một trong hai dict mà không có trong dict kia
    for key in dict1.keys() | dict2.keys():
        new_path = f"{path}.{key}" if path else key
        
        if key not in dict1:
            differences.append(f"Key '{new_path}' chỉ có trong file thứ hai, dòng {line_num + 1}")
        elif key not in dict2:
            differences.append(f"Key '{new_path}' chỉ có trong file thứ nhất, dòng {line_num + 1}")
        else:
            # Kiểm tra giá trị của các key
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                # Nếu cả hai giá trị đều là dict, gọi đệ quy để so sánh
                differences.extend(compare_dicts(dict1[key], dict2[key], new_path, lines1, lines2, line_num))
            elif dict1[key] != dict2[key]:
                # Nếu khác nhau, ghi nhận sự khác biệt và dòng
                differences.append(f"Dòng khác nhau tại '{new_path}': {dict1[key]} != {dict2[key]}, dòng {line_num + 1}")
    
    return differences

def compare_toml(file1, file2):
    """So sánh hai file TOML và in ra các sự khác biệt, bao gồm dòng số."""
    toml1, lines1 = load_toml_with_lines(file1)
    toml2, lines2 = load_toml_with_lines(file2)
    
    differences = compare_dicts(toml1, toml2, lines1=lines1, lines2=lines2)
    
    if differences:
        print("Các sự khác biệt:")
        for diff in differences:
            print(diff)
    else:
        print("Hai file TOML này hoàn toàn giống nhau.")


# Sử dụng hàm để so sánh hai file TOML
file1 = "/workspaces/k8sconfig_edit/indent/step4_thut.toml"
file2 = "/workspaces/k8sconfig_edit/tom_edit/config.toml"
compare_toml(file1, file2)
