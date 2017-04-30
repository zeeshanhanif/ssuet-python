filename = 'data.txt'
with open(filename) as file_object:
    for line in file_object:
        #sublines = line.split('t')
        sublines = line.split()
        for sl in sublines:
            print(sl)
