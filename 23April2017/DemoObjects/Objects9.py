class Dog():

    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        print("Hello World in init")

    def sit(self):
        print(self)
        print("hello "+self.name)

myDog = Dog("willie",6)
myDog.email = "willie@gmail.com"
print(myDog.email)

myDog2 = Dog("Lucy",7)
print(myDog2);
print(myDog2.email)

print("")
print("")
