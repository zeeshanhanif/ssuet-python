import json

#numbers = [2, 3, 5, 7, 11, 13]
numbers = {"hello":"world", 34:"test", True:45}

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)