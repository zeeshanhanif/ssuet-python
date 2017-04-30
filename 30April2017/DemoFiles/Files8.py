filename = 'data.txt'
with open(filename) as file_object:
    count = 0;
    for line in file_object:
        count+=1
        print(line)
        if count == 2:
            break
