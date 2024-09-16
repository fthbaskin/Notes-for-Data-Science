import json


# You can store a dictionary as a json file
example_dict = {1: "1", 2: "2", 3: "3"}
json_text = json.dumps(example_dict)
with open("example.json", "w", encoding='utf-8') as f:
    f.write(json_text)

# You can load a json file or text as a dictionary
json_text_example = '{"1": 1, "2": 2, "3": 3}'
json_dict_example = json.loads(json_text_example)
for key, value in json_dict_example.items():
    print(key, value)
