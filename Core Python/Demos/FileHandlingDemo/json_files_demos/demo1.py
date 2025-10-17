import json
data = {
    "101": {
        "name": "EMP-101",
        "age": 25,
        "languages": [
            "English",
            "Spanish"
        ]
    },
    "102": {
        "name": "EMP-102",
        "age": 28,
        "languages": [
            "English",
            "Spanish"
        ]
    },
    "103": {
        "name": "EMP-103",
        "age": 27,
        "languages": [
            "English",
            "Spanish"
        ]
    },
    "104": {
        "name": "EMP-104",
        "age": 32,
        "languages": [
            "English",
            "Spanish"
        ]
    }
}

with open("Core Python/Demos/FileHandlingDemo/json_files_demos/emp_data.json","w+") as fp:
    json.dump(data,fp,indent=4)
