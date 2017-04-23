class Dog():

    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        print("Hello World in init")

    def sit(self):
        print(self)
        print("hello "+self.name)

myDog = Dog("willie",6)
print(myDog);
print(myDog.name)
#print(myDog.email)
myDog.sit()