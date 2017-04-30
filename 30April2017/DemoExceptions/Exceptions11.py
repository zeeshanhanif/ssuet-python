class Student():
    def __init__(self, name, age):
        if age > 70:
            raise StudentAgeException("Age can not be greater then 70")
        self.name = name;
        self.age =age;

class StudentAgeException(Exception):
    pass


#st = Student("Faisal",150);
try:
    st = Student("Faisal",50);
except StudentAgeException:
    print("Age Error");
else :
    print(st.age);