import json


with open("Core Python/Demos/FileHandlingDemo/json_files_demos/emp_data.json", "r") as fp:
    data = json.load(fp)

# Convert Python object → JSON string
json_str = json.dumps(data)
print(json_str)

# Convert JSON string → Python object
data_back = json.loads(json_str)
print(data_back)
