class Human():

    def __init__(self,name,age):
        self.name = name;
        self.age = age;

    def sleep(self):
        print("Human is sleeping")

class Student(Human):

    def __init__(self,course):
        super().__init__("hello",45)
        self.course = course;
        print("Hello in student init")

    def study(self):
        print("Hello in student")

    def sleep(self):
        print("Student is sleeping")


class Course():

    def __init__(self,name):
        self.name=name

    def doSomeWork(self):
        print("do somework")

c = Course("Python")
s = Student(c);
print(s.name);
print(s.course.name);
s.course.doSomeWork()

