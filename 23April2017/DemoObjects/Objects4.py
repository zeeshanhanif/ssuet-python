class Dog():

    def __init__(self):
        print("Hello World in init")

    def sit(self):
        print(self)
        print("hello World")

myDog = Dog()
print(myDog);
myDog.sit()