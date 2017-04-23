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
myDog.name = "Lucy"
print(myDog.name)
myDog.sit()
print("")
print("")
myDog.email = "lucy@gmail.com"
print(myDog.email)
