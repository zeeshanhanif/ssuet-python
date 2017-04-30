try:
    print(5/1)
    #open("abc.txt")
except ZeroDivisionError:
    print("ZeroDivisionError!")
except FileNotFoundError:
    print("FileNotFoundError!")
except:
    print("Error!")
finally:
    print("Finally");