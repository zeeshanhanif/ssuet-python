class Human():

    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    def sleep(self):
        print("Human is sleeping")

class Student(Human):



    def study(self):
        print("Hello in student")



h = Human("Usman",36)
print(h.name);
s = Student("Arbaz",35);
print(s.name);