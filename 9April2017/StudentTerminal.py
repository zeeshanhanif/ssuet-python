
studentslist = ["zeeshan","saad","osama"]


print("Welcome to student portal")
print("Please enter 1 to list student names")
print("Please enter 2 to add student names")
print("Please enter 3 to search student names")
print("Please enter 4 to delete particular student names")
print("Please enter 5 to sort student names")
print("enter 6 to exit")

while(True):
    user_input = int(input("Enter of your choice"))

    if user_input == 1:
        for studentnames in studentslist:
            print(studentnames)
    elif user_input == 2:
        addname = input("Enter name to add")
        studentslist.append(addname)
        print(studentslist)
    elif user_input == 3:
        userinput = input("Search for a student name")
        if userinput in studentslist:
            print("found")
        else:
            print("not found")
    elif user_input == 4:
        userinput = input("Enter student name to delete")
        if userinput in studentslist:
            studentslist.remove(userinput)
            print(userinput + " deleted")
        else:
            print("not found")

    elif user_input == 5:

            studentslist.sort()
            print("Sorted")
            print(studentslist)

    elif user_input == 6:
        exit()

