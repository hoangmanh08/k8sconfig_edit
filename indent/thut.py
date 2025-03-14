import re

def split_str(input_str):
    # Bước 1: Loại bỏ dấu [ và ]  
    cleaned_str = input_str.strip("[]")  

    # Bước 2: Tách chuỗi bởi dấu "  
    parts = cleaned_str.split('"')  

    # Bước 3: Xử lý và tạo danh sách kết quả  
    result = []  

    for i, part in enumerate(parts):  
        if i % 2 == 0:  # Phần bên ngoài dấu "  
            sub_parts = part.split('.')  
            result.extend([sub_part for sub_part in sub_parts if sub_part])  # Thêm các phần không rỗng  
        else:  # Phần nằm trong dấu "  
            result.append(part)  # Thêm phần nằm giữa dấu "  

    # Bước 4: Kết hợp các phần bên trong  
    if len(result) > 1:  
        # Kết hợp tất cả các phần nằm trong dấu "  
        combined_inner = '.'.join(result[1:2])  # Chỉ cần phần nằm trong dấu "  
        result = [result[0], combined_inner] + result[2:]  # Thay thế và giữ lại các phần còn lại  

    # In kết quả  
    return result

def same(all_values, i):
    # Kiểm tra số lượng giá trị giống nhau giữa các danh sách liên tiếp  
    current_list = all_values[i]  
    next_list = all_values[i - 1]  

    # Tìm các giá trị giống nhau  
    common_values = set(current_list) & set(next_list)  

    # In kết quả  
    # # print(f"Các giá trị giống nhau giữa danh sách {i} và danh sách {i + 1}: {common_values}")  
    # print(f"Số lượng giá trị giống nhau giữa danh sách {i} và danh sách {i - 1}: {len(common_values)}")  
    return len(common_values)

def count_same(all_values, i):
    # Chọn danh sách hiện tại (có thể thay đổi chỉ số)  
    current_list = all_values[i]  # Ví dụ: chọn danh sách a  
    # print(f"\nDanh sách hiện tại: {current_list}")  

    # Biến để theo dõi số lượng lớn nhất  
    max_common_count = 0  

    # Kiểm tra số lượng giá trị giống nhau  
    for i, other_list in enumerate(all_values):  
        if other_list is not current_list:  # Chỉ so sánh với danh sách khác  
            # Tìm các giá trị giống nhau  
            common_values = set(current_list) & set(other_list)  
            common_count = len(common_values)  # Đếm số giá trị giống nhau  

            # Cập nhật số lượng lớn nhất nếu cần  
            if common_count > max_common_count:  
                max_common_count = common_count  

    # # In ra số lượng giá trị giống nhau lớn nhất  
    # print(f"Số lượng giá trị giống nhau lớn nhất giữa danh sách hiện tại và các danh sách khác: {max_common_count}")  
    return max_common_count

def format_toml(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = []
    indent_level = 0
    # prev_section = ""
    nhay = []
    flag = True

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith("[") and stripped_line.endswith("]"):
            flag = False
        if flag:
            result.append(stripped_line)
            continue

        

        if stripped_line.startswith("[") and stripped_line.endswith("]"):
            # flag = False
            nhay.append(split_str(stripped_line))

            if len(nhay) == 1:
                result.append(stripped_line)
                continue


            indent_level = same(nhay, len(nhay)-1)

            # if indent_level == 0:
            #     # Câu lệnh hoặc comment giữ nguyên nhưng được thụt lề theo indent_level
            #     indent = "    " * (indent_level)
            #     result.append(indent + stripped_line)
            #     continue

            # # Kiểm tra mức độ lồng nhau bằng cách so sánh với phần tử trước đó
            # if stripped_line.startswith(prev_section) and prev_section:
            #     indent_level += 1
            # else:
            #     indent_level = 1 if prev_section else 0
            
            # prev_section = stripped_line  # Cập nhật phần tử trước đó
            indent = "  " * indent_level
            result.append(indent + stripped_line)
        else:
            # Câu lệnh hoặc comment giữ nguyên nhưng được thụt lề theo indent_level
            indent = "  " * (indent_level + 1)
            result.append(indent + stripped_line)

    # Ghi kết quả vào file đầu ra
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(result) + "\n")

# Sử dụng hàm
format_toml("step3_lui.toml", "step4_thut.toml")
