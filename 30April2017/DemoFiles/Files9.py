filename = 'data.txt'
with open(filename) as file_object:
    for line in file_object:
        #print(line)
        textToSearch = "lazy"
        if textToSearch in line:
            print("Found "+textToSearch+" in line ");
            print(line);