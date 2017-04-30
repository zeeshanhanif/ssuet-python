try:
    result = 5/1
    #open("abc.txt")
except ZeroDivisionError:
    print("ZeroDivisionError!")
else :
    print("result "+str(result))
finally:
    print("finnaly")
