filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("FileNotFoundError");
else:
    print("in else")
