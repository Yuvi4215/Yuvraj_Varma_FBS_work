import json

# Read from a JSON file


with open("Core Python/Demos/FileHandlingDemo/json_files_demos/emp_data.json", "r") as fp:
    data = json.load(fp)



for k,v in data.items():
    print(f"{k} : {v}")