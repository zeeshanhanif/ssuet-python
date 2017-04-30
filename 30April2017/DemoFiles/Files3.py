#myFile = open('D:\\developmentData\\DeepLearning\\projects\\ssuet-python\\30April2017\\DemoFiles\\hello\\work.txt');
#myFile = open('hello\\work.txt');
myFile = open('data.txt');
lines = myFile.readlines()

for line in lines:
    print(line.rstrip());
