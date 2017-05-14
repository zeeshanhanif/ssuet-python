from functools import partial
def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
#twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
twice_xs = map(double, xs)
for x1 in twice_xs:
    print(x1)
#twice_xs = map(double, xs)

print("----")

def multiply(x, y): return x * y

products = map(multiply, [1, 2,3], [4, 5,6])
for x1 in products:
    print(x1)

print("----")

def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 != 0
x_evens = [x for x in xs if is_even(x)]
print(x_evens)


