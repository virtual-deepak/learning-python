import json

def read_json(file_name, is_pretty, indent):
    with open(file_name, 'r') as file:
        json_data = json.load(file)
        if is_pretty:
            print(json.dumps(json_data, indent=indent))
        else:
            print(json.dumps(json_data)) # Similar to: print(json_data)

read_json('./samples/files_to_read/authors.json', True, 4)
