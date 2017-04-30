class Student():
    def __init__(self, name, age):
        if age > 70:
            raise StudentAgeException("Age can not be greater then 70")
        self.name = name;
        self.age =age;

class StudentAgeException(Exception):
    pass


#st = Student("Faisal",150);
st = Student("Faisal",10);
print(st.age);