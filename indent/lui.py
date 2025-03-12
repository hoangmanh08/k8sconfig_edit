def transform_toml_content(toml_content):
    lines = toml_content.splitlines()
    transformed_lines = []
    plugins_section_added = False
    stream_processors_section_added = False
    
    for line in lines:
        
        # Thêm phần [plugins] nếu chưa có và gặp dòng [plugins. đầu tiên
        if line.startswith('[plugins.') and not plugins_section_added:
            transformed_lines.append('[plugins]\n')
            plugins_section_added = True
        elif line.startswith('[stream_processors.') and not stream_processors_section_added:
            transformed_lines.append('[stream_processors]\n')
            stream_processors_section_added = True

        
        
        # Thêm dòng vào danh sách kết quả
        transformed_lines.append(line)
    
    # Kết hợp các dòng trở lại thành một chuỗi
    return '\n'.join(transformed_lines)

# Đọc nội dung từ file input.toml

with open('/workspaces/k8sconfig_edit/yam_tom_output2.toml', 'r') as input_file:
    toml_content = input_file.read()

# Chuyển đổi nội dung
transformed_content = transform_toml_content(toml_content)

# Ghi nội dung đã chuyển đổi vào file output.toml
with open('lui_output.toml', 'w') as output_file:
    output_file.write(transformed_content)

print("Chuyển đổi thành công! Kết quả đã được lưu vào file output.toml")
    