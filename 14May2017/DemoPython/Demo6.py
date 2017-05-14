
def doSomeWork(*args):
    for x in args:
        print(x)

#doSomeWork(3,5,3,4,5,6,7,8,8)

def doSomeWork(**kwargs):
    for x in kwargs:
        print(x,kwargs[x])

doSomeWork(a="hello",b="work",c="test")