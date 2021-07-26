import base64
import oss2, requests, json, os

def get_b64(s):
    json_str = s.encode('utf-8')
    return base64.b64encode(json_str).decode('utf-8')


def get_dynamic_outputs( outputs, d_output_len, file_ext_list):
    dynamic_outputs = []
    output_len = len(outputs)
    output = outputs[output_len-1]
    dir = os.path.dirname(output)
    base_name = os.path.basename(output)
    for i in range(d_output_len):
        if i < len(file_ext_list):
            file_ext = file_ext_list[i]
        else:
            file_ext = file_ext_list[len(file_ext_list)-1]
        base_name_fixed = f"{base_name[:base_name.rfind('_')]}_{output_len+i}.{file_ext}"
        dynamic_outputs.append(os.path.join(dir, base_name_fixed))
    return dynamic_outputs
