import pandas as pd
import yaml

def convert_excel_to_yaml(excel_file, yaml_file):
    df = pd.read_excel(excel_file)

    yaml_dict = {}
    
    for _, row in df.iterrows():
        keys = row["Parameter"].split(".")
        value = row["Setup Value"]

        flag = False

        # Chuyển đổi giá trị thành kiểu phù hợp  
        if pd.isna(value):  # Kiểm tra nếu value là NaN (trống)  
            value = ""  # Gán None vào value thay vì bỏ qua  
        elif isinstance(value, str) and value.upper() == "TRUE":  
            value = True  
        elif isinstance(value, str) and value.upper() == "FALSE":  
            value = False  
        elif isinstance(value, float) and value.is_integer():  
            value = int(value)  
        
        # if isinstance(value, str) and value.upper() == "TRUE":
        #     value = True
        # elif isinstance(value, str) and value.upper() == "FALSE":
        #     value = False
        # elif isinstance(value, float) and value.is_integer():
        #     value = int(value)


        
        temp = yaml_dict

        # for key in keys[:-1]:
        #     if "annotation" in key:
        #         last_key = row["Parameter"]
        #         temp = temp.setdefault(last_key, {})
        #         temp[last_key] = value
        #         flag = True
        #         break
        # if flag:
        #     continue

        # # Kiểm tra xem có chứa từ khóa "annotation"  
        # if any("annotation" in key for key in keys[:-1]):  # Kiểm tra xem trong keys có từ khóa "annotation" không  
        #     last_key = row["Parameter"]  
        #     temp[last_key] = value  # Gán giá trị vào từ điển yaml_dict  
        #     continue  # Bỏ qua phần còn lại và tiếp tục với dòng tiếp theo  

        
        
        for key in keys[:-1]:
            if key == "io" and keys[keys.index(key)-1] == "timeouts" :
                
                index = keys.index(key)  
                spec = '.'.join(keys[index:])
                # spec = \" + spec + \"
                # last_key = row["Parameter"]  
                temp[spec] = value
                flag = True
                break 

            if "[" in key and "]" in key: 
                base_key, index = key.split("[")
                index = int(index.rstrip("]"))
                temp = temp.setdefault(base_key, [])
                while len(temp) <= index:
                    temp.append({})
                temp = temp[index]
            else:
                temp = temp.setdefault(key, {})

        if flag:
            continue

        last_key = keys[-1]
        if "[" in last_key and "]" in last_key: 
            base_key, index = last_key.split("[")
            index = int(index.rstrip("]"))
            temp = temp.setdefault(base_key, [])
            while len(temp) <= index:
                temp.append(None)
            temp[index] = value
        else:
            temp[last_key] = value


    with open(yaml_file, "w") as f:
        yaml.dump(yaml_dict, f, default_flow_style=False, sort_keys=False)

    print(f"Done!")

if __name__ == "__main__":
    input_excel = "/workspaces/k8sconfig_edit/tom_edit/config.toml.xlsx" 
    output_yaml = "step1_main.yaml"  
    convert_excel_to_yaml(input_excel, output_yaml)
