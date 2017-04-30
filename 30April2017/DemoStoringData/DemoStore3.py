import json

numberList = [2, 3, 5, 7, 11, 13]
numbers = {
    "hello":"world", 34:"test", True:45,
    "data": numberList
    }

filename = 'numbers2.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)