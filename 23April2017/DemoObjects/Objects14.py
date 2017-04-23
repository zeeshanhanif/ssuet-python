class Human():

    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    def sleep(self):
        print("Human is sleeping")

class Student(Human):

    def __init__(self):
        super().__init__("hello",45)
        print("Hello in student init")

    def study(self):
        print("Hello in student")



h = Human("Usman",36)
print(h.name);
s = Student();
print(s.name);

s.sleep()