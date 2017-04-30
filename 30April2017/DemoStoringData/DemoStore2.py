import json

filename = 'numbers.json'
with open(filename, 'r') as f_obj:
    data = json.load(f_obj)

print(data)
print(data["hello"])