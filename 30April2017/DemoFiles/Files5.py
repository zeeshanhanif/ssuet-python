#myFile = open('D:\\developmentData\\DeepLearning\\projects\\ssuet-python\\30April2017\\DemoFiles\\hello\\work.txt');
#myFile = open('hello\\work.txt');

with open('data.txt') as myFile:
    lines = myFile.readlines()
#------------------


print(myFile)
print(lines)