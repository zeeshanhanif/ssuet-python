st = {"name":"Ishaq", "age":34, "email":"abc1@gmail.com"}
st1 = {"name":"Usman", "age":35, "email":"abc2@gmail.com"}
st2 = {"name":"Arbaz", "age":36, "email":"abc3@gmail.com"}
st3 = {"name":"Adnan", "age":37, "email":"abc4@gmail.com"}

students = {
    "1": st,
    "2": st1,
    "3": st2,
    "4": st3
}
#1
print(students["2"]);
#2
print(students["2"]["name"]);
#3
stNew = students["3"]
print(stNew["name"])
