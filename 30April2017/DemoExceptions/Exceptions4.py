try:
    print(5/0)
    #open("abc.txt")
except ZeroDivisionError:
    print("ZeroDivisionError!")
except FileNotFoundError:
    print("FileNotFoundError!")
except:
    print("Error!")