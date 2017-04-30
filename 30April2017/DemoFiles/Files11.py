filename = 'data.txt'
with open(filename) as file_object:
   with open("newData.txt","w") as newFile:
       for rLines in file_object:
           newFile.write(rLines)

