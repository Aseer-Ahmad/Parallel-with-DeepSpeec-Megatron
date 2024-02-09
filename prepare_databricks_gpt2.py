#fine_tune_gpt2.py

import os
import sys
import json

PARENT_PTH = os.getcwd()
JSON_PTH   = 'dataset/databricks-dolly-15k.jsonl'
JSON_W_PTH = 'dataset/databricks-dolly-15k_mod.jsonl'
DATA_PTH   = os.path.join(PARENT_PTH, JSON_PTH)
count_lines = 0
def load_json_string(json_string):
    try:
        # Use json.loads to convert the string to a dictionary
        data_dict = json.loads(json_string)
        return data_dict
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

str_write = ""

with open(DATA_PTH, 'r') as file:
    for line in file:
        dict_json = load_json_string(line.strip())
        dict_json['text'] = str(dict_json["context"]) + " " + str(dict_json['instruction']) + " " + str(dict_json['response'])
        str_write += json.dumps(dict_json) + "\n"
        count_lines += 1

with open( os.path.join(PARENT_PTH, JSON_W_PTH), 'w') as file:
    file.write(str_write)

print(f"{JSON_PTH} rows : {count_lines}\n{JSON_W_PTH} rows : {len(str_write.splitlines())} written. ")

