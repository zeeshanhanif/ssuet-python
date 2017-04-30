class MyException(Exception):
    pass

try:
    raise MyException("Incorrect data")
    #open("work.txt")
except FileNotFoundError as e:
    print("FileNotFoundError");
except MyException as e:
    print("MyException");
else:
    print("in else")

