class Dog():

    def __init__(self):
        self.name = "Dog";
        self.age = 9;
        print("Hello World in init")

    def sit(self):
        print(self)
        print("hello "+self.name)

myDog = Dog()
myDog.name="Lucy";
print(myDog.name)